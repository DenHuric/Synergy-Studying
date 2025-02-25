document.addEventListener("DOMContentLoaded", () => {
  const addNoteButton = document.getElementById("add-note");
  const noteInput = document.getElementById("note-input");
  const notesContainer = document.getElementById("notes-container");

  // Загрузить заметки из localStorage
  const loadNotes = () => {
    const notes = JSON.parse(localStorage.getItem("notes")) || [];
    notesContainer.innerHTML = "";
    notes.forEach((noteText, index) => {
      createNoteElement(noteText, index);
    });
  };

  // Сохранить заметки в localStorage
  const saveNotes = (notes) => {
    localStorage.setItem("notes", JSON.stringify(notes));
  };

  // Создать элемент заметки
  const createNoteElement = (noteText, index) => {
    const note = document.createElement("div");
    note.classList.add("note");

    const noteContent = document.createElement("span");
    noteContent.textContent = noteText;
    note.appendChild(noteContent);

    // Кнопка редактирования
    const editButton = document.createElement("button");
    editButton.textContent = "✏️";
    editButton.onclick = () => {
      const newText = prompt("Редактировать заметку:", noteText);
      if (newText) {
        const notes = JSON.parse(localStorage.getItem("notes")) || [];
        notes[index] = newText;
        saveNotes(notes);
        loadNotes();
      }
    };
    note.appendChild(editButton);

    // Кнопка удаления
    const deleteButton = document.createElement("button");
    deleteButton.textContent = "❌";
    deleteButton.onclick = () => {
      const notes = JSON.parse(localStorage.getItem("notes")) || [];
      notes.splice(index, 1);
      saveNotes(notes);
      loadNotes();
    };
    note.appendChild(deleteButton);

    notesContainer.appendChild(note);
  };

  // Добавить заметку
  addNoteButton.onclick = () => {
    const noteText = noteInput.value.trim();
    if (noteText) {
      const notes = JSON.parse(localStorage.getItem("notes")) || [];
      notes.push(noteText);
      saveNotes(notes);
      loadNotes();
      noteInput.value = "";
    }
  };

  // Загрузить заметки при инициализации
  loadNotes();
});
