async function generateCampaign() {
  document.getElementById("form-container").style.display = "none";

  document.getElementById("loading-screen").style.display = "block";

  setTimeout(() => {
    resizeCanvas();
  }, 50);
  try {
    const response = await fetch("/generate-content", {
      method: "POST",
      headers: {
        "Content-Type": "application/json",
      },
      body: JSON.stringify({
        product: document.getElementById("product").value,

        audience: document.getElementById("audience").value,

        brand_description: document.getElementById("brandDescription").value,
      }),
    });

    const data = await response.json();

    window.generatedCampaign = data;

    document.querySelector(".loader").style.display = "none";

    document.getElementById("loading-title").innerText = "✅ Campaña generada";

    document.getElementById("loading-subtitle").innerText =
      "Tu campaña está lista.";

    document.getElementById("view-results-btn").style.display = "inline-block";
  } catch (error) {
    alert("Error generating campaign");

    console.error(error);
  }
}

function showResult(data) {
  document.getElementById("loading-screen").style.display = "none";

  document.getElementById("chat-container").style.display = "flex";

  const chat = document.getElementById("chat-messages");

  //   chat.innerHTML = "";

  const campaignResult = `
📢 Campaign Name

${data.campaign_name}

────────────────────────

🎯 Concept

${data.concept}

────────────────────────

🎨 Tone

${data.tone}

────────────────────────

📸 Instagram

${data.instagram_post}

────────────────────────

📘 Facebook

${data.facebook_post}

────────────────────────

💼 LinkedIn

${data.linkedin_post}

────────────────────────

${data.approved ? "✅ Compliance Approved" : "❌ Compliance Rejected"}
`;

  addMessage(chat, campaignResult);
}

function showGeneratedResults() {
  showResult(window.generatedCampaign);
}

function addMessage(chat, text) {
  const msg = document.createElement("div");

  msg.className = "message";

  msg.textContent = text;

  chat.appendChild(msg);

  chat.scrollTop = chat.scrollHeight;
}

async function sendChatMessage() {
  const input = document.getElementById("chat-input");

  const text = input.value.trim();

  if (!text) return;

  const chat = document.getElementById("chat-messages");

  addMessage(chat, "👤 " + text);

  input.value = "";

  try {
    const response = await fetch("/chat", {
      method: "POST",
      headers: {
        "Content-Type": "application/json",
      },
      body: JSON.stringify({
        message: text,
      }),
    });

    if (!response.ok) {
      throw new Error("Server error");
    }

    const data = await response.json();

    // ===========================
    // Reception Agent
    // ===========================

    if (data.status === "GENERAL") {
      addMessage(chat, "🤖 " + data.message);

      return;
    }

    // ===========================
    // Editor Agent
    // ===========================

    addMessage(chat, "🤖 " + data.message);

    window.generatedCampaign = data.campaign;

    showResult(data.campaign);
  } catch (error) {
    console.error(error);

    addMessage(chat, "🤖 Error: " + error.message);
  }
}

const canvas = document.getElementById("canvasCarga");

const ctx = canvas.getContext("2d");

function resizeCanvas() {
  canvas.width = canvas.offsetWidth;

  canvas.height = canvas.offsetHeight;

  ctx.fillStyle = "#000";

  ctx.fillRect(0, 0, canvas.width, canvas.height);
}

window.addEventListener("resize", resizeCanvas);

let drawing = false;

let lastX = 0;
let lastY = 0;

let hue = 0;

ctx.lineWidth = 6;
ctx.lineCap = "round";

function startDraw(e) {
  drawing = true;

  lastX = e.offsetX;
  lastY = e.offsetY;
}

function draw(e) {
  if (!drawing) return;

  ctx.beginPath();

  ctx.moveTo(lastX, lastY);

  ctx.lineTo(e.offsetX, e.offsetY);

  ctx.strokeStyle = `hsl(${hue},100%,50%)`;

  ctx.stroke();

  hue = (hue + 2) % 360;

  lastX = e.offsetX;
  lastY = e.offsetY;
}

function stopDraw() {
  drawing = false;
}

canvas.addEventListener("mousedown", startDraw);

canvas.addEventListener("mousemove", draw);

canvas.addEventListener("mouseup", stopDraw);

canvas.addEventListener("mouseleave", stopDraw);
