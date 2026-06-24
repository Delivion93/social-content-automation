const canvas = document.getElementById("networkCanvas");

const ctx = canvas.getContext("2d");

function resize() {
  canvas.width = window.innerWidth;

  canvas.height = window.innerHeight;
}

resize();

window.addEventListener("resize", resize);

const particles = [];

for (let i = 0; i < 70; i++) {
  particles.push({
    x: Math.random() * canvas.width,

    y: Math.random() * canvas.height,

    vx: (Math.random() - 0.5) * 0.4,

    vy: (Math.random() - 0.5) * 0.4,
  });
}

function animate() {
  ctx.clearRect(0, 0, canvas.width, canvas.height);

  for (const p of particles) {
    p.x += p.vx;

    p.y += p.vy;

    if (p.x < 0 || p.x > canvas.width) p.vx *= -1;

    if (p.y < 0 || p.y > canvas.height) p.vy *= -1;
  }

  for (let i = 0; i < particles.length; i++) {
    const a = particles[i];

    ctx.beginPath();

    ctx.arc(a.x, a.y, 2, 0, Math.PI * 2);

    ctx.fillStyle = "#5b7cff";

    ctx.fill();

    for (let j = i + 1; j < particles.length; j++) {
      const b = particles[j];

      const dx = a.x - b.x;

      const dy = a.y - b.y;

      const dist = Math.sqrt(dx * dx + dy * dy);

      if (dist < 150) {
        ctx.beginPath();

        ctx.moveTo(a.x, a.y);

        ctx.lineTo(b.x, b.y);

        ctx.strokeStyle = `rgba(91,124,255,${1 - dist / 150})`;

        ctx.stroke();
      }
    }
  }

  requestAnimationFrame(animate);
}

animate();
