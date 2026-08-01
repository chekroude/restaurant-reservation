const API_URL = "http://localhost:5000/api";

/**
 * Wrapper autour de fetch() : ajoute automatiquement le token JWT
 * s'il existe, et centralise la gestion des erreurs.
 */
async function apiCall(endpoint, method = "GET", body = null) {
    const headers = { "Content-Type": "application/json" };
    const token = localStorage.getItem("token");
    if (token) headers["Authorization"] = `Bearer ${token}`;

    const options = { method, headers };
    if (body) options.body = JSON.stringify(body);

    const response = await fetch(`${API_URL}${endpoint}`, options);
    const data = await response.json();

    if (!response.ok) {
        throw new Error(data.error || "Une erreur est survenue");
    }
    return data;
}
