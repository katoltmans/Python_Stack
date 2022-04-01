console.log("File run successfully upon loading page for first time");

function gitInfo() {
    console.log("got data");
    
    fetch("https://api.github.com/users/katoltmans")
        // Take data from HTML object and extract JSON
        .then(response => response.json() )
        // Redraw page
        .then(data => {
            console.log(data);
            // If wanting to clear pageXOffset
            var mainPage = document.getElementById("content");
            mainPage.innerHTML = ""; // Clear everything inside the container
            /* Create buttons for navigation */
            //var row = document.createElement("div");
            //row.setAttribute("class", "row");

            //mainPage.innerHTML = JSON.stringify(data);
            var selectedOptions = document.getElementById("select_get_key_name").selectedOptions;
            var select_value_array = [].map.call(selectedOptions, option => option.value);
            console.log(select_value_array)
            for (var i=0; i<select_value_array.length; i++){
                var select_value_string = select_value_array[i]
                if (select_value_string == "name"){
                    mainPage.innerHTML += "<strong>User Name: " + data[select_value_string] + "</strong><br>"
                }
                else if (select_value_string == "location") {
                    mainPage.innerHTML += "<strong>Lives In: " + data[select_value_string] + "</strong><br>"
                }
                else if (select_value_string == "avatar_url") {
                    mainPage.innerHTML += "<img src='" + data[select_value_string] + "' alt='avatar' width='100' height='130'><br>"
                }
                else if (select_value_string == "followers") {
                    mainPage.innerHTML += "<strong>Number of Followers: " + data[select_value_string] + "</strong><br>"
                }
                else if (select_value_string == "public_repos") {
                    mainPage.innerHTML += "<strong>Public repos available: " + data[select_value_string] + "</strong><br>"
                }
            }
            
        })
        .catch(err => console.log(err));
        return false;
}

// Function could also be written:
//  var response = await fetch("https://api.github.com/users/katoltmans")
// Use await function to request does not time out
    // Convert data to JSON format
//    var userData = await response.json();
//    console.log(userData)
//    return userData;