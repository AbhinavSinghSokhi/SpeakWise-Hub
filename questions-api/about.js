let aboutMessage = 'AI Soft Skills.Your gateway to mastering the art of effective communication.';

function setMessage(_, { message } ) {
    aboutMessage = message;
    return aboutMessage;
}

function getMessage() {
    return aboutMessage;
}

module.exports = { getMessage, setMessage };