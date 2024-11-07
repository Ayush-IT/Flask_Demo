// document.addEventListener("DOMContentLoaded", function () {
//     const form = document.getElementById("movieForm");
//     form.onsubmit = async (event) => {
//         event.preventDefault();

//         const formData = new FormData(form);
//         const response = await fetch('/add_movie', {
//             method: 'POST',
//             body: formData
//         });

//         if (response.ok) {
//             const movie = await response.json();
//             const movieList = document.getElementById("movieList");
//             movieList.innerHTML += `<li>${movie.title} (${movie.release_year})</li>`;
//             form.reset();
//         }
//     };
// });
