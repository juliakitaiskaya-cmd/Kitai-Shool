<?php
/**
 * Прокси: Tilda Webhook  ->  Bitrix24 (коробка) crm.lead.add
 * Залить на свой сервер (с PHP), напр.: https://ВАШ-ДОМЕН/tilda-to-bitrix.php
 * В Tilda: Настройки сайта -> Формы -> Webhook -> указать адрес этого файла (POST).
 */

// --- Входящий вебхук Bitrix24 (CRM) ---
$WEBHOOK = 'https://cp.znanied.ru/rest/1/9qd1yzt0ag25frq2/';

// --- Данные из формы Tilda ---
$name  = trim($_POST['Name']  ?? $_POST['name']  ?? '');
$phone = trim($_POST['Phone'] ?? $_POST['phone'] ?? '');

// --- Поля лида ---
$fields = array(
    'TITLE'     => 'Заявка с сайта — пробный урок (Kitai School)',
    'NAME'      => $name,
    'SOURCE_ID' => 'WEB',
    'OPENED'    => 'Y',
    'PHONE'     => array(array('VALUE' => $phone, 'VALUE_TYPE' => 'WORK')),
);

// --- UTM-метки (если есть скрытые поля в форме) ---
foreach (array('utm_source','utm_medium','utm_campaign','utm_content','utm_term') as $u) {
    if (!empty($_POST[$u])) {
        $fields[strtoupper($u)] = trim($_POST[$u]);
    }
}

// --- Доп. служебные поля Tilda в комментарий (необязательно) ---
$comment = '';
if (!empty($_POST['formname'])) { $comment .= 'Форма: '.$_POST['formname']."\n"; }
if (!empty($_POST['tranid']))   { $comment .= 'Tilda ID: '.$_POST['tranid']."\n"; }
if ($comment !== '') { $fields['COMMENTS'] = trim($comment); }

// --- Вызов crm.lead.add ---
$payload = http_build_query(array(
    'fields' => $fields,
    'params' => array('REGISTER_SONET_EVENT' => 'Y'),
));

$ch = curl_init($WEBHOOK . 'crm.lead.add.json');
curl_setopt_array($ch, array(
    CURLOPT_POST           => true,
    CURLOPT_POSTFIELDS     => $payload,
    CURLOPT_RETURNTRANSFER => true,
    CURLOPT_TIMEOUT        => 15,
    CURLOPT_SSL_VERIFYPEER => true,
));
$response = curl_exec($ch);
$err = curl_error($ch);
curl_close($ch);

// (необязательно) лог для отладки — раскомментируй при настройке:
// file_put_contents(__DIR__.'/tilda-bitrix.log', date('c')."\nPOST: ".json_encode($_POST, JSON_UNESCAPED_UNICODE)."\nRESP: ".$response."\nERR: ".$err."\n\n", FILE_APPEND);

// Tilda ожидает 200 OK
http_response_code(200);
header('Content-Type: application/json; charset=utf-8');
echo json_encode(array('status' => 'ok'));
