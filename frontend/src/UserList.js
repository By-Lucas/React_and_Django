import React from 'react';
import ListComponent from './ListComponent';

export default class UserLists extends React.Component{
    /* Fazer conexao com api + token */
    state = { lists: [], loading: true}

    /*Autorização via token*/
    async componentDidMount(){
        const config = {
            headers: {
                'Content-Type': 'application/json'
            }
        }
        config.headers['Authorization'] = 'token ' + localStorage.getItem('token');

        var url = 'http://127.0.0.1:8000/list/';
        const response = await fetch(url, config);
        const data = await response.json();
        console.log(data);
        this.setState({lists: data, loading: true});
    }

    render() 
    {
        const listApi = this.state.lists;
        return (
            <div>
                {listApi.map(list => <ListComponent key={list.id} listName={list.name} items={list.item_set}/>)}
            </div>
        )
    }
}