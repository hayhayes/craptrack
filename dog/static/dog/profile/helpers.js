// page reset helper
export function setPage(page, title) {
  page.title.textContent = title;
  page.dashboard.innerHTML = "";
}

export function createButton(text, onClick) {
  const btn = document.createElement("button");
  btn.type = "button";
  btn.className = "btn btn-primary my-3";
  btn.textContent = text;
  btn.addEventListener("click", onClick);
  return btn;
}

export function createTable(headers, includeActions = false) {
  const table = document.createElement("table");
  table.className = "table table-striped";

  const thead = document.createElement("thead");
  const tr = document.createElement("tr");

  headers.forEach(text => {
    const th = document.createElement("th");
    th.scope = "col";
    th.textContent = text;
    tr.appendChild(th);
  });

  if (includeActions) {
    const th = document.createElement("th");
    th.scope = "col";
    th.textContent = "Actions";
    tr.appendChild(th);
  }

  thead.appendChild(tr);
  table.appendChild(thead);

  const tbody = document.createElement("tbody");
  table.appendChild(tbody);

  return { table, tbody };
}

export function renderRows(tbody, rows) {
  tbody.innerHTML = ""; // optional: rerender cleanly
  const fragment = document.createDocumentFragment();

  rows.forEach(row => {
    const tr = document.createElement("tr");

    row.forEach(cell => {
      const td = document.createElement("td");
      td.textContent = cell;
      tr.appendChild(td);
    });

    /*if (onEdit || onDelete) {
      const td = document.createElement("td");

      if (onEdit) {
        const editBtn = document.createElement("button");
        editBtn.className = "btn btn-sm btn-outline-primary me-2";
        editBtn.textContent = "Edit";
        editBtn.addEventListener('click', () => onEdit(row.id));
        td.appendChild(editBtn);
      }

      if (onDelete) {
        const deleteBtn = document.createElement("button");
        deleteBtn.className = "btn btn-sm btn-outline-danger";
        deleteBtn.textContent = "Delete";
        deleteBtn.addEventListener('click', () => onDelete(row.id));
        td.appendChild(deleteBtn);
      }

      tr.appendChild(td);
    }*/

    fragment.appendChild(tr);
  });

  tbody.appendChild(fragment);
}


export function createInput(name, type, labelText) {
  const div = document.createElement("div");
  div.className = "mb-3";

  const label = document.createElement("label");
  label.textContent = labelText;
  label.className = "form-label";

  const input = document.createElement("input");
  input.type = type;
  input.name = name;
  input.className = "form-control";
  input.required = true;

  div.append(label, input);
  return div;
}

export function addOptions(options, select){
  options.unshift({id: "", name: "--Please Select an Option--"});
  options.forEach(opt => {
    const option = document.createElement("option");
    option.value = typeof opt === 'object' ? opt.id : opt;
    option.textContent = typeof opt === 'object' ? opt.name : opt;
    select.appendChild(option);
  });
}

export function createSelect(name, labelText, options) {
  const div = document.createElement("div");
  div.className = "mb-3";

  const label = document.createElement("label");
  label.textContent = labelText;
  label.className = "form-label";

  const select = document.createElement("select");
  select.name = name;
  select.className = "form-select";
  select.required = true;

  addOptions(options, select);

  div.append(label, select);
  return div;
}

export function add_form(type) {
  const form = document.querySelector(`form#${type}`);
  form.style.display = 'block';
}
