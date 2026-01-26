console.log("Script")

const form = document.getElementById("traductor-form");
const resultadoDiv = document.getElementById("resultado");
const textoTraducido = document.getElementById("texto-traducido");
const errorDiv = document.getElementById("error");

form.addEventListener("submit", async (e) => {
    e.preventDefault();

    resultadoDiv.classList.add("oculto");
    errorDiv.classList.add("oculto");

    const texto = document.getElementById("texto").value;
    const origen = document.getElementById("origen").value;
    const destino = document.getElementById("destino").value;

    try {
        const response = await fetch("http://localhost:8000/traducir", {
            method: "POST",
            headers: {
                "Content-Type": "application/json"
            },
            body: JSON.stringify({
                texto: texto,
                origen: origen,
                destino: destino
            })
        });

        const data = await response.json();

        if (!response.ok) {
            throw new Error(data.detail || "Error en la traducción");
        }

        textoTraducido.textContent = data.traduccion;
        resultadoDiv.classList.remove("oculto");

    } catch (error) {
        errorDiv.textContent = error.message;
        errorDiv.classList.remove("oculto");
    }
});
