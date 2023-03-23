function deleteNote(noteId) {
    fetch("/delete-note", {
      method: "POST",
      body: JSON.stringify({ noteId: noteId }),
    }).then((_res) => {
      window.location.href = "/";
    });
  }

/* The deleteNote function is called when the user clicks the delete button. It sends a POST request to the 
 /delete-note endpoint with the noteId as the body. The server then deletes the note from the database 
 and redirects the user to the homepage. */