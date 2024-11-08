$(document).ready(function() {
    // AJAX form submission
    $('#movieForm').on('submit', function(event) {
        event.preventDefault();
        let title = $('#title').val();
        let releaseYear = $('#release_year').val();

        // Submit form data using AJAX
        $.ajax({
            url: '/add_movie',
            type: 'POST',
            data: { title: title, release_year: releaseYear },
            success: function(response) {
                // If success, add the new movie card to the list
                if (response.title && response.release_year) {
                    $('#movieList').append(
                        `<div class="movie-card">
                            <h3>${response.title}</h3>
                            <p>Release Year: ${response.release_year}</p>
                        </div>`
                    );
                    // Clear form inputs
                    $('#movieForm')[0].reset();
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
