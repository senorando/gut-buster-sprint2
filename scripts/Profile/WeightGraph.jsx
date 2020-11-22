import React, { useState, useEffect } from 'react';

import { Tooltip, LineChart, Line, XAxis, YAxis, CartesianGrid, Legend,} from "recharts";

export function WeightGraph(props) {
    const userWeight = props.userWeight;
    
    const weight_data = [
        { name: "weight1", Weight: userWeight[ userWeight.length - 7] },
        { name: "weight2", Weight: userWeight[ userWeight.length - 6] },
        { name: "weight3", Weight: userWeight[ userWeight.length - 5] },
        { name: "weight4", Weight: userWeight[ userWeight.length - 4] },
        { name: "weight5", Weight: userWeight[ userWeight.length - 3] },
        { name: "weight6", Weight: userWeight[ userWeight.length - 2] },
        { name: "weight7", Weight: userWeight[ userWeight.length - 1] },
    ];
    return (
        <div className = 'WeightGraph'>
            <h3>Last 7 Weight Entries</h3>
            <LineChart width={400} height={150} data={weight_data}>
                <Line type="monotone" dataKey="Weight" stroke="#8884d8" strokeWidth={2}  labelLine={true} label/>
            </LineChart>
        </div>
    )
}