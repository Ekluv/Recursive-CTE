import 'whatwg-fetch';

function parseJSON(response) {
  return response.json();
}

function checkStatus(response) {
  if (response.status >= 200 && response.status < 300 && response.ok) {
    return response;
  }

  const error = new Error(response.statusText);
  error.response = response.json();
  throw error;
}


export default function request(url, payload, method='POST') {
  let options;
  if (payload) {
    const data = JSON.stringify(payload);
    options = {
      method: method,
      headers: {
        'Content-Type': 'application/json',
      },
      credentials: 'same-origin',
      body: data,
    };
  }
  return fetch(url, options)
    .then(parseJSON)
    .catch((error) => {
      console.error('API Error: ', error);
      if(error.response.message) {
        window.alert(error.response.message);
      }
      
    });
}

