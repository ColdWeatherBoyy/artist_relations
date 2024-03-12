document.addEventListener("DOMContentLoaded", function () {
	const searchForm = document.getElementById("artist-search-form");
	const inputField = document.getElementById("artist-search-input");

	searchForm.addEventListener("submit", function (event) {
		if (!inputField.value.trim()) {
			event.preventDefault();
			alert("Please enter an artist name");
		}
	});
});
