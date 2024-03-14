document.addEventListener("DOMContentLoaded", function () {
	const searchForm = document.getElementById("artist-search-form");
	const inputField = document.getElementById("artist-search-input");
	const formButton = document.getElementById("artist-search-button");

	searchForm.addEventListener("submit", function (event) {
		if (!inputField.value.trim()) {
			event.preventDefault();
			alert("Please enter an artist name");
			return;
		}
		// disable the button, change its cursor, and make it look like its thinking
		formButton.disabled = true;
		formButton.style.cursor = "wait";
		formButton.style.backgroundColor = "white";
		formButton.style.color = "#7266db";
		formButton.classList.add("continuous-pulse");
		inputField.style.pointerEvents = "none";
		inputField.blur();
		inputField.style.opacity = "0.2";
	});
});
