const btn4Text = document.getElementById("btn4-text");
const eventb = document.getElementById("eventb");

eventb.addEventListener("click", () => {
  btn4Text.classList.remove("hidden");
  btn4Text.classList.add("popup-message");
});

btn4Text.addEventListener("animationend", () => {
  btn4Text.classList.remove("popup-message");
  btn4Text.classList.add("hidden");
});

const btn4Text1 = document.getElementById("btn4-text1");
const eventb1 = document.getElementById("eventb1");

eventb1.addEventListener("click", () => {
  btn4Text1.classList.remove("hidden1");
  btn4Text1.classList.add("popup-message");
});

btn4Text1.addEventListener("animationend", () => {
  btn4Text1.classList.remove("popup-message");
  btn4Text1.classList.add("hidden1");
});

// static/script.js

function vote(value) {
  const eventb = document.getElementById("voteValue");
  voteValueInput.value = value;
}

document.getElementById("gachaButton").addEventListener("click", playGacha);

function playGacha() {
  var themes = [
    "テーマ：好みのスタイルは？",
    "テーマ：新しく服を買うなら？",
    "テーマ：新しく服を買うなら？",
    "テーマ：最先端のスタイルは？",
  ];

  var randomTheme1 = themes[Math.floor(Math.random() * themes.length)];
  var randomImagePath1 =
    imagePath1[Math.floor(Math.random() * imagePath1.length)];
  var randomImagePath2 =
    imagePath2[Math.floor(Math.random() * imagePath2.length)];

  var gachaResults = document.getElementById("gachaResults");
  gachaResults.innerHTML = `
      <h3>${randomTheme1}</h3>
      <ul class="card-list">
        <li class="card">
            <img src="${randomImagePath1}" alt="Image 1" height="400px">
            <a class="card-description">
                <h2>A</h2>
            </a>
        </li>
        <li class="card">
            <img src="${randomImagePath2}" alt="Image 2" height="400px">
            <a class="card-description">
                <h2>B</h2>
            </a>
        </li>
      </ul>
 
 
  `;
}
