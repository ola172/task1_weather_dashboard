const loadingEl = document.getElementById("loading");
const errorEl = document.getElementById("error");
const weatherCard = document.getElementById("weatherCard");
const cityInput = document.getElementById("cityInput");
let lastUpdatedEl = document.getElementById("lastUpdated");

let debounceTimer = null;
const DEBOUNCE_MS = 800;

function setLoading(isLoading) {
  loadingEl.classList.toggle("hidden", !isLoading);
}

function showError(message) {
  errorEl.textContent = message;
  errorEl.classList.remove("hidden");
}

function hideError() {
  errorEl.classList.add("hidden");
}

function renderWeather(data) {
  document.getElementById("location").textContent = data.location_name ?? "-";
  document.getElementById("status").textContent = data.weather_status ?? "-";
  document.getElementById("description").textContent = data.weather_description ?? "-";
  document.getElementById("temp").textContent = (data.temperature ?? "-").toFixed?.(1) ?? "-";
  document.getElementById("feels_like").textContent = (data.feels_like ?? "-").toFixed?.(1) ?? "-";
  document.getElementById("humidity").textContent = data.humidity ?? "-";
  document.getElementById("pressure").textContent = data.pressure ?? "-";
  document.getElementById("wind_speed").textContent = data.wind_speed ?? "-";
  document.getElementById("wind_direction").textContent = data.wind_direction ?? "-";
  document.getElementById("wind_gust").textContent = data.wind_gust ?? "-";
  document.getElementById("clouds_percentage").textContent = data.clouds_percentage ?? "-";
  document.getElementById("visibility").textContent = data.visibility ?? "-";
  document.getElementById("sunrise").textContent = data.sunrise ? new Date(data.sunrise * 1000).toLocaleTimeString() : "-";
  document.getElementById("sunset").textContent = data.sunset ? new Date(data.sunset * 1000).toLocaleTimeString() : "-";
  document.getElementById("temp_min").textContent = data.temp_min ?? "-";
  document.getElementById("temp_max").textContent = data.temp_max ?? "-";
  document.getElementById("icon").src = data.icon
    ? `https://openweathermap.org/img/wn/${data.icon}@2x.png`
    : "https://via.placeholder.com/64";

  const now = new Date().toLocaleTimeString();
  lastUpdatedEl.textContent = `Last updated: ${now}`;
  weatherCard.classList.remove("hidden");
}

async function fetchWeather(params) {
  try {
    setLoading(true);
    hideError();

    let endpoint = "";
    let body = {};

    if (params.city) {
      endpoint = "/api/weather/city";
      body = { city: params.city, units: "metric" };
    } else if (params.lat && params.lon) {
      endpoint = "/api/weather/coords";
      body = { lat: params.lat, lon: params.lon, units: "metric" };
    } else {
      throw new Error("Missing parameters for weather request.");
    }

    const res = await fetch(endpoint, {
      method: "POST",
      headers: { "Content-Type": "application/json" },
      body: JSON.stringify(body),
    });

    if (!res.ok) {
      const errorData = await res.json();
      throw new Error(errorData.detail || "Unable to fetch weather data.");
    }

    const data = await res.json();
    renderWeather(data);
  } catch (err) {
    showError(err.message);
  } finally {
    setLoading(false);
  }
}

// Search button click handler
const searchBtn = document.querySelector(".input-section button");
searchBtn.addEventListener("click", () => {
  const city = cityInput.value.trim();
  if (city) fetchWeather({ city });
});

// Initialize geolocation on load
window.addEventListener("DOMContentLoaded", () => {
  if (navigator.geolocation) {
    setLoading(true);
    navigator.geolocation.getCurrentPosition(
      (pos) => {
        fetchWeather({ lat: pos.coords.latitude, lon: pos.coords.longitude });
      },
      (err) => {
        console.warn("Geolocation failed:", err.message);
        showError("Unable to detect your location. Please enter a city manually.");
        setLoading(false);
      },
      { timeout: 7000 }
    );
  }
});
