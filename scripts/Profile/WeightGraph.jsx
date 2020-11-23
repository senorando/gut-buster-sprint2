import React from 'react';
import {LineChart, Line, XAxis, YAxis, CartesianGrid, Tooltip, Legend,} from 'recharts';
export function WeightGraph(props) {
    const userWeight = props.userWeight;
    
    const weight_data = [
        { name: "weight1", UserWeight: userWeight[ userWeight.length - 7], GoalWeight: 125 },
        { name: "weight2", UserWeight: userWeight[ userWeight.length - 6], GoalWeight: 125 },
        { name: "weight1", UserWeight: userWeight[ userWeight.length - 7], GoalWeight: 125 },
        { name: "weight3", UserWeight: userWeight[ userWeight.length - 5], GoalWeight: 125 },
        { name: "weight4", UserWeight: userWeight[ userWeight.length - 4], GoalWeight: 125 },
        { name: "weight5", UserWeight: userWeight[ userWeight.length - 3], GoalWeight: 125 },
        { name: "weight6", USerWeight: userWeight[ userWeight.length - 2], GoalWeight: 125 },
        { name: "weight7", UserWeight: userWeight[ userWeight.length - 1], GoalWeight: 125 },
    ];
    return (
        <div className = 'WeightGraph'>
            <LineChart
            width={500}
            height={300}
            data={weight_data}
            margin={{ top: 5, right: 30, left: 20, bottom: 5, }}>
        <CartesianGrid strokeDasharray="3 3" />
        <XAxis dataKey="name" />
        <YAxis />
        <Tooltip />
        <Legend />
        <Line type="monotone" dataKey="UserWeight" stroke="#8884d8" activeDot={{ r: 8 }} />
        <Line type="monotone" dataKey="GoalWeight" stroke="#82ca9d" />
      </LineChart>
        </div>
    )
}