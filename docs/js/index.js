
var data_url = "https://raw.githubusercontent.com/Blankscreen-exe/docker-practice/main/data/data.json"

// Load the data.json file
fetch(data_url)
    .then(response => response.json())
    .then(data => {

        // Initialize DataTables
        $(document).ready(function () {
            $('#data-table').DataTable({
                responsive: true,
                ajax: {
                    url: data_url,
                    dataSrc: ''
                },
                columns: [ {
                    "targets": 0,
                    "data": 'id',
                    "searchable": true,
                    "render": function (data, type) {
                        return `<span class="serial-number">${data.toString().padStart(3, "0")}</span>`;
                    }
                  },
                  {
                    "targets": 1,
                    "data": 'status',
                    "searchable": false,
                    "render": function (data, type) {
                        if (data === "Done") {
                            return `<span class="status-item" title=" Done ">🔵</span>`;
                        } else if (data === "WIP") {
                            return `<span class="status-item" title=" WIP ">🟡</span>`;
                        } else if (data === "Not Started") {
                            return `<span class="status-item" title=" Not Started ">🔴</span>`;
                        } else {
                            return `<span class="status-item" title=" N/A ">⚪️</span>`;
                        }   
                    }
                  },
                  {
                    "targets": [2,3],
                    "data": 'topic',
                    "searchable": true,
                    "render": function (data, type) {
                        return data.link != ""
                            ? `<a title="Go To Tutorial" class="tutorial-link" target="_blank" href="https://github.com/Blankscreen-exe/docker-practice/tree/main${data.link}">${data.title}</a>`
                            : `<span title="Tutorial Not Available" class="tutorial-link disabled-link">${data.title}</span>`;
                    } 
                  },
                  {
                    "targets": [4],
                    "data": 'tags',
                    "searchable": true,
                    "render": function (data, type) {
                        return "<span class='tag-container'>" + data.map( part => `<span class="tag-item">${part}</span>` ).join(' ') + "</span>";
                    }
                  }
                 ]
            });
        });
    })
    .catch(error => console.error('Error loading data:', error));
