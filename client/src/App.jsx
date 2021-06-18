import React from 'react';
import axios from 'axios';


class App extends React.Component {
  constructor(props) {
  super(props);
  this.state = {
    data: [],

  };
}
componentDidMount() {
    axios.get('http://0.0.0.0:8080/course/')
    .then(res => {
        this.setState({
            data: res.data
        });
    })
    .catch(err => {})
}

render() {
    return (
      <ul>
        {this.state.data.map(course => {
          return (
            <div key={course.id}>
              <h1>{course.name}</h1>
              <h2>Описание</h2>
              <p>{course.description}</p>
              <p>Начало <b>{course.start_date}</b></p>
              <p>Окончание <b>{course.end_date}</b></p>
              <p>Количество участников <b>{course.students_count}</b></p>
            </div>
          );
        })}
      </ul>
    );
  }
}


export default App;
