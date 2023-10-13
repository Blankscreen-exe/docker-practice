console.log("HULLO DUM DUMS")

var data_url = "https://raw.githubusercontent.com/Blankscreen-exe/docker-practice/main/docs/data/data.json"

// Load the data.json file
fetch(data_url)
    .then(response => response.json())
    .then(data => {
        const tableBody = document.querySelector('#data-table tbody');

        data.forEach(entry => {
            const row = document.createElement('tr');
            const idCell = document.createElement('td');
            const statusCell = document.createElement('td');
            const topicCell = document.createElement('td');
            const tagsCell = document.createElement('td');

            // topicCell.colSpan = 2;

            idCell.innerHTML = `<span class="serial-number">${entry.id.toString().padStart(3, "0")}</span>`;
            topicCell.innerHTML = `<a title="Go To Tutorial" class="tutorial-link" href="${entry.folderLink}">${entry.topic}</a>`;
            tagsCell.innerHTML = "<span class='tag-container'>" + entry.tags.map( part => `<span class="tag-item">${part}</span>` ).join(' ') + "</span>";
            if (entry.status === "Done") {
                statusCell.innerHTML = `<span class="status-item" title=" Done ">🔵</span>`;
            } else if (entry.status === "WIP") {
                statusCell.innerHTML = `<span class="status-item" title=" WIP ">🟡</span>`;
            } else if (entry.status === "Not Started") {
                statusCell.innerHTML = `<span class="status-item" title=" Not Started ">🔴</span>`;
            } else {
                statusCell.innerHTML = `<span class="status-item" title=" N/A ">⚪️</span>`;
            }

            row.appendChild(idCell);
            row.appendChild(statusCell);
            row.appendChild(topicCell);
            row.appendChild(tagsCell);

            // MSG: logging
            console.log(idCell);
            console.log(statusCell);
            console.log(topicCell);
            console.log(tagsCell);

            tableBody.appendChild(row);
        });

        // Initialize DataTables
        $(document).ready(function () {
            $('#data-table').DataTable();
        });
    })
    .catch(error => console.error('Error loading data:', error));
