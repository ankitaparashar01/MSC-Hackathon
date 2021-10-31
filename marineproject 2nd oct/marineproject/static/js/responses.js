// function getBotResponse(input) {
//     if (input == "Progress?") {
//         return "You are done with 50% of Module 1";
//     }
//     else if (input == "Next task?") {
//         return "Your next task is Module 1 Checkpoint 3";
//     }

//     // greetings
//     if (input == "Hello") {
//         return "Hello there!";
//     }
//     else if (input == "goodbye") {
//         return "Talk to you later!";
//     }
//     else {
//         return "Try asking something else!";
//     }
// }

function getBotResponse(input) {
    //rock paper scissors
    if (input == "Progress?") {
        return "You are 50% done with Module 1";
    } else if (input == "Next Task?") {
        return "You need to do Module 1 Checkpoint 3 next";
    } 

    // Simple responses
    if (input == "hello") {
        return "Hello there!";
    } else if (input == "goodbye") {
        return "Talk to you later!";
    } else {
        return "Try asking something else!";
    }
}

