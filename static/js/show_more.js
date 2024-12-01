const button = document.getElementById('show-more');
button.addEventListener('click', loadMore); {
};

function show_more(){
    console.log('yesser')
}

let currentPage = 1; // set the initial page to 1

function loadMore() {
  // Increment the current page
  currentPage++;

  // Send an AJAX request to the /load_more route with the current page parameter
  $.ajax({
    url: '/load_more',
    data: { page: currentPage },
    type: 'GET',
    success: function(response) {
      // Get the players-container div element
      const playersContainer = document.getElementById('players-container');

      // Loop through the response data and create a new HTML element for each player
        response.forEach(function(player) {
        const playerRow = document.createElement('tr');
        playerRow.classList.add('new-row'); // Add the CSS class to the new row

        const rankCell = document.createElement('td');
        rankCell.textContent = player.RANK;
        playerRow.appendChild(rankCell);

        const nameCell = document.createElement('td');
        nameCell.textContent = player.NAME;
        playerRow.appendChild(nameCell);

        const teamCell = document.createElement('td');
        teamCell.textContent = player.TEAM;
        playerRow.appendChild(teamCell);

        const positionCell = document.createElement('td');
        positionCell.textContent = player.POS;
        playerRow.appendChild(positionCell);

        const ageCell = document.createElement('td');
        ageCell.textContent = player.AGE;
        playerRow.appendChild(ageCell);

        const PPGCell = document.createElement('td');
        PPGCell.textContent = player.PPG;
        playerRow.appendChild(PPGCell);

        const RPGCell = document.createElement('td');
        RPGCell.textContent = player.RPG;
        playerRow.appendChild(RPGCell);

        const APGCell = document.createElement('td');
        APGCell.textContent = player.APG;
        playerRow.appendChild(APGCell);

        const SPGCell = document.createElement('td');
        SPGCell.textContent = player.SPG;
        playerRow.appendChild(SPGCell);

        // Add the new player row to the table
        playersContainer.querySelector('tbody').appendChild(playerRow);


        /*
        const playerElement = document.createElement('div');
        playerElement.innerHTML = `${player.RANK} - ${player.NAME} - ${player.TEAM}`;
        playersContainer.appendChild(playerElement);
        */
      });
    },
    error: function(error) {
      // Handle any errors that occur during the AJAX request
      console.error(error);
    }
  });
}






/*
function loadMore() {
    // Set the page parameter to 2
    const page = 2;
  
    // Send an AJAX request to the /load_more route with the page parameter
    $.ajax({
      url: '/load_more',
      data: { page: page },
      type: 'GET',
      success: function(response) {
        // Handle the response from the server
        console.log(response);
      },
      error: function(error) {
        // Handle any errors that occur during the AJAX request
        console.error(error);
      }
    });
  }
*/

