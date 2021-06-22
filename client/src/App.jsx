import React from 'react';
import axios from 'axios';


class App extends React.Component {
  constructor(props) {
  super(props);
  this.state = {data: [], value: ''};
  this.handleChange = this.handleChange.bind(this);
  this.handleSubmit = this.handleSubmit.bind(this);
}

handleChange(event) {this.setState({value: event.target.value}); }
handleSubmit(event) {alert('Отправленное имя: ' + this.state.value);}

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
      <div>
      <form onSubmit={this.handleSubmit}>
        <label>
          Имя:
          <input type="text" value={this.state.value} onChange={this.handleChange} />
          </label>
        <input type="submit" value="Отправить" />
      </form>

      <ul>
        {this.state.data.map(course =>
            <div key={course.id}>
              <h1>{course.name}</h1>
              <h2>Описание</h2>
              <p>{course.description}</p>
              <p>Начало <b>{course.start_date}</b></p>
              <p>Окончание <b>{course.end_date}</b></p>
              <p>Количество участников <b>{course.students_count}</b></p>
            </div>          
        )}
      </ul>
      </div>
    );
  }
}


export default App;
