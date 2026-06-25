async function generateCampaign() {
  const form = document.getElementById("form-container");
  const loading = document.getElementById("loading-screen");

  form.classList.remove("screen-visible");
  form.classList.add("screen-hidden");

  setTimeout(() => {
    form.style.display = "none";

    loading.style.display = "block";

    requestAnimationFrame(() => {
      loading.classList.remove("screen-hidden");
      loading.classList.add("screen-visible");

      initializeCanvas();
    });
  }, 450);

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
  const loading = document.getElementById("loading-screen");
  const chatContainer = document.getElementById("chat-container");

  loading.classList.remove("screen-visible");
  loading.classList.add("screen-hidden");

  setTimeout(() => {
    loading.style.display = "none";

    chatContainer.style.display = "flex";
    initializeChat();

    requestAnimationFrame(() => {
      chatContainer.classList.remove("screen-hidden");
      chatContainer.classList.add("screen-visible");
    });
  }, 450);

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

  if (text.startsWith("👤")) {
    msg.classList.add("user-message");
  } else {
    msg.classList.add("assistant-message");
  }

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

  const typing = document.createElement("div");

  typing.className = "message assistant-message";

  typing.id = "typing-indicator";

  typing.innerHTML = `
🤖 Procesando...

<div class="typing">
    <span></span>
    <span></span>
    <span></span>
</div>
`;

  chat.appendChild(typing);

  chat.scrollTop = chat.scrollHeight;

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
    document.getElementById("typing-indicator")?.remove();

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
    document.getElementById("typing-indicator")?.remove();
    addMessage(chat, "🤖 Error: " + error.message);
  }
}

let canvas = null;
let ctx = null;

function initializeCanvas() {
  canvas = document.getElementById("canvasCarga");

  if (!canvas) return;

  ctx = canvas.getContext("2d");

  ctx.lineWidth = 6;
  ctx.lineCap = "round";

  resizeCanvas();

  canvas.addEventListener("mousedown", startDraw);
  canvas.addEventListener("mousemove", draw);
  canvas.addEventListener("mouseup", stopDraw);
  canvas.addEventListener("mouseleave", stopDraw);
}

function resizeCanvas() {
  if (!canvas || !ctx) return;

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

function initializeChat() {
  const input = document.getElementById("chat-input");

  if (!input) return;

  input.addEventListener("keydown", function (event) {
    if (event.key === "Enter") {
      event.preventDefault();

      sendChatMessage();
    }
  });
}
