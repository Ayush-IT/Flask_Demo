$(document).ready(function() {
  // AJAX form submission
  $('#movieForm').on('submit', function(event) {
      event.preventDefault();
      let title = $('#title').val();
      let releaseYear = $('#release_year').val();

      // Submit form data using AJAX
      $.ajax({
          url: '/add_movie',  // URL to POST data
          type: 'POST',
          data: { title: title, release_year: releaseYear },
          success: function(response) {
              // If success, update the movie list with the full list returned from the server
              if (response.movies) {
                  $('#movieList').empty();  // Clear the existing movie list
                  // Loop through the updated movies and append them to the movie list container
                  response.movies.forEach(function(movie) {
                      $('#movieList').append(
                          `<div class="movie-card">
                              <h3>${movie.title}</h3>
                              <p>Release Year: ${movie.release_year}</p>
                          </div>`
                      );
                  });
                  // Clear form inputs (only on display page)
                  if ($('#title').length) {
                      $('#movieForm')[0].reset();
                  }
              } else {
                  alert("Error adding movie.");
              }
          },
          error: function() {
              alert("Error with the request.");
          }
      });
  });
});

