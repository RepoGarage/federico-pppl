const taskForm = document.getElementById("taskForm");
const taskInput = document.getElementById("taskInput");
const todoList = document.getElementById("todoList");
const modalOverlay = document.getElementById("modalOverlay");
const confirmDeleteBtn = document.getElementById("confirmDelete");
const cancelDeleteBtn = document.getElementById("cancelDelete");

let tasks = [];
let taskToDelete = null;

// Helper to create button with icon
function createIconButton(btnClass, iconPath, alt, text) {
  const btn = document.createElement("button");
  btn.className = btnClass;
  btn.type = "button";
  const img = document.createElement("img");
  img.src = iconPath;
  img.alt = alt;
  img.width = 18;
  img.height = 18;
  btn.appendChild(img);
  btn.appendChild(document.createTextNode(text));
  return btn;
}

function renderTasks() {
  todoList.innerHTML = "";
  tasks.forEach((task, i) => {
    const li = document.createElement("li");
    li.className = "todo-item";

    if (task.editing) {
      const input = document.createElement("input");
      input.type = "text";
      input.value = task.text;
      input.className = "task-input";
      input.autofocus = true;

      let saveBtn;
      input.addEventListener("keydown", function (e) {
        if (e.key === "Enter") {
          saveBtn.click();
        }
      });

      const actionsDiv = document.createElement("div");
      actionsDiv.className = "todo-actions";

      saveBtn = createIconButton(
        "edit-btn",
        "./components/icons8-edit-32.png",
        "Save",
        "Save"
      );
      saveBtn.onclick = () => {
        const newText = input.value.trim();
        if (newText !== "") {
          tasks[i].text = newText;
          tasks[i].editing = false;
          renderTasks();
        } else {
          input.focus();
          input.style.borderColor = "#ef4444";
        }
      };
      actionsDiv.appendChild(saveBtn);

      const cancelBtn = createIconButton(
        "cancel-btn",
        "./components/icons8-edit-32.png",
        "Cancel",
        "Cancel"
      );
      cancelBtn.onclick = () => {
        tasks[i].editing = false;
        renderTasks();
      };
      actionsDiv.appendChild(cancelBtn);

      li.appendChild(input);
      li.appendChild(actionsDiv);

      setTimeout(() => input.focus(), 0);
    } else {
      const span = document.createElement("span");
      span.className = "todo-text";
      span.textContent = task.text;
      li.appendChild(span);

      const actionsDiv = document.createElement("div");
      actionsDiv.className = "todo-actions";

      const editBtn = createIconButton(
        "edit-btn",
        "./components/icons8-edit-32.png",
        "Edit",
        "Edit"
      );
      editBtn.onclick = () => {
        // Only one task in edit mode at a time
        tasks.forEach((t, idx) => {
          t.editing = idx === i;
        });
        renderTasks();
      };
      actionsDiv.appendChild(editBtn);

      const deleteBtn = createIconButton(
        "delete-btn",
        "./components/icons8-trash.svg",
        "Delete",
        "Delete"
      );
      deleteBtn.onclick = () => {
        taskToDelete = i;
        modalOverlay.classList.remove("hidden");
      };
      actionsDiv.appendChild(deleteBtn);

      li.appendChild(actionsDiv);
    }

    todoList.appendChild(li);
  });
}

taskForm.addEventListener("submit", function (e) {
  e.preventDefault();
  const value = taskInput.value.trim();
  if (value !== "") {
    // Reset all editing state when adding new task
    tasks.forEach((t) => (t.editing = false));
    tasks.push({ text: value });
    taskInput.value = "";
    renderTasks();
  }
});

confirmDeleteBtn.addEventListener("click", function () {
  if (taskToDelete !== null) {
    tasks.splice(taskToDelete, 1);
    taskToDelete = null;
    modalOverlay.classList.add("hidden");
    renderTasks();
  }
});
cancelDeleteBtn.addEventListener("click", function () {
  taskToDelete = null;
  modalOverlay.classList.add("hidden");
});
modalOverlay.addEventListener("click", function (e) {
  if (e.target === modalOverlay) {
    modalOverlay.classList.add("hidden");
    taskToDelete = null;
  }
});
renderTasks();
