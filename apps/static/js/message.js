// WebSocketのインスタンスを作成する
const ws = new WebSocket(
  "wss://ec25-240f-cd-100d-1-80c4-d807-984-dbf4.ngrok-free.app/ws"
);

// 自分のメッセージID
const _sentMessageId = Math.random().toString(36).slice(-10);

// WebSocketのイベントハンドラ
// 接続
ws.onopen = () => {
  console.log("Connected to the websocket");
};

/* メッセージ受信
 *  受信するメッセージの形式
 *  message = {
 * 		id: string, // メッセージID
 * 		text: string, // メッセージ本文
 * 		time: string // 送信時刻
 * }
 */
ws.onmessage = (e) => {
  const message = JSON.parse(e.data);
  // 自分が送信したメッセージは表示しない
  if (_sentMessageId === message.id) {
    return;
  }
  // 受信したメッセージを表示する
  showSentMsg(message.text);
};

/**
 * メッセージ送信
 *  送信できるメッセージの形式
 *  payload = {
 * 		id: string, // メッセージID
 * 		text: string, // メッセージ本文
 * 		time: string // 送信時刻
 * }
 */
function sendMessage() {
  const messageInput = document.getElementById("message");
  // メッセージを送信する
  const payload = {
    id: _sentMessageId,
    text: messageInput.value,
    time: "",
  };
  // メッセージを送信する
  ws.send(JSON.stringify(payload));
  // 自分が送信したメッセージを表示する
  showSentMsg(payload.text);
}

// 送受信の吹き出しを表示
function showSentMsg(message) {
  // メッセージの吹き出しを作成
  const logArea = document.getElementById("log");
  let msgBubbleStr = `
		<div class="chat">
			<div class="chat-bubble @color-class@">
				<pre class="whitespace-pre-wrap">
					@message@
				</pre>
			</div>
		</div>
	`;
  msgBubbleStr = msgBubbleStr.replace("@message@", message);
  logArea.innerHTML += msgBubbleStr;

  // 一番下までスクロール
  logArea.scrollTop = logArea.scrollHeight;
}
