$(document).ready(function () {
  $("#movieForm").on("submit", function (event) {
    event.preventDefault();
    let title = $("#title").val();
    let releaseYear = $("#release_year").val();

    $.ajax({
      url: "/add_movie",
      type: "POST",
      data: { title: title, release_year: releaseYear },
      success: function (response) {
        if (response.title && response.release_year) {
          alert("Movie added successfully!");
          // Clear form inputs
          $("#movieForm")[0].reset();
        } else {
          alert("Error adding movie.");
        }
      },
      error: function () {
        alert("Error with the request.");
      },
    });
  });
});
