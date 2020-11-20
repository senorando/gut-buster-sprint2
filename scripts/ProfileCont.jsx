import React, { useState, useEffect } from 'react';
import { UpdateForm } from './UpdateForm';
import { Socket } from './Socket';
import { PieChart,  Pie, Sector, Cell, Tooltip,LineChart, Line, XAxis, YAxis, CartesianGrid, Legend,} from "recharts";
export function ProfileCont(props){
    console.log(props);
    const currentUser = props.currentUser;
    const [isEdit, setStatus] = useState(false);
    const profileDetail = props.profileDetail;
    const userWeight = props.userWeight;
    const data = [
                { name: "MaxCalories", Macros: profileDetail.maxCal },
                { name: "MaxProtine", Macros: profileDetail.maxProt },
                { name: "Maxcarb", Macros: profileDetail.maxCarb },
                { name: "MaxFat", Macros: profileDetail.maxFat },
             ];
    const COLORS = ['#0088FE', '#00C49F', '#FFBB28', '#FF8042'];
    const RADIAN = Math.PI / 180;
    const renderCustomizedLabel = ({
        cx, cy, midAngle, innerRadius, outerRadius, percent, index,
        }) => {
        const radius = innerRadius + (outerRadius - innerRadius) * 0.5;
        const x = cx + radius * Math.cos(-midAngle * RADIAN);
        const y = cy + radius * Math.sin(-midAngle * RADIAN);

         return (
                    <text x={x} y={y} fill="white" textAnchor={x > cx ? 'start' : 'end'} dominantBaseline="central">
                     {`${(percent * 100).toFixed(0)}%`}
                     </text>
                );
        };
    const weight_data = [
        { name: "weight1", Weight: userWeight[ userWeight.length - 4] },
        { name: "weight2", Weight: userWeight[ userWeight.length - 3] },
        { name: "weight3", Weight: userWeight[ userWeight.length - 2] },
        { name: "weight4", Weight: userWeight[ userWeight.length - 1] },
    ];
    function updateStatus() {
        console.log('isEdit: ' + isEdit);
        setStatus((prevStatus) => !isEdit);
    }
    Socket.on('not editing', (data) => {
        console.log(data);
        setStatus(false);
    });
    Socket.off('not editing', '');
    return (
        <div>
            <div id = 'UserDetails'>
                <h1> { currentUser.name } </h1><br/>
                <label>Height: { profileDetail.height }</label><br/>
                <label>Weight: { userWeight[ userWeight.length - 1 ] }</label><br/>
                <label>Age: { profileDetail.age }</label><br/>
                <label>Gender: { profileDetail.gender }</label><br/>
                <label>Activity Level: { profileDetail.activityLevel }</label><br/>
                <label>BMR: { profileDetail.bmr }</label><br/>
                { isEdit? 
                    <div id = 'UserForm'>
                        <UpdateForm currentUser = { currentUser }/>
                    </div>
                    :
                    <button onClick = { updateStatus }>Add New Weight Entry</button>
                }
            </div>
            <div id = 'Macros'>
                <h3>Recommended Macros based on your goals</h3><br/>
                <label>Max Calories: { profileDetail.maxCal }</label><br/>
                <label>Max Protein: { profileDetail.maxProt }</label><br/>
                <label>Max Carbs: { profileDetail.maxCarb }</label><br/>
                <label>Max Fat: { profileDetail.maxFat }</label><br/>
            </div>
            <div id = 'Recommended Meals'>
                <h3>Recommended Meals based on your macros</h3>
                <label>Breakfast: { profileDetail.breakfastMeal }</label><br/>
                <label>Lunch: { profileDetail.lunchMeal }</label><br/>
                <label>Dinner: { profileDetail.dinnerMeal }</label><br/>
                <label>Total Calories: { profileDetail.calMeal }</label><br/>
                <label>Total Protein: { profileDetail.protMeal }</label><br/>
                <label>Total Carbs: { profileDetail.carbMeal }</label><br/>
                <label>Total Fat: { profileDetail.fatMeal }</label><br/>
            </div>
             <div>
                <h3> Pie Chart Of Macros </h3>
                <PieChart width={400} height={400}>
                <Pie
                    dataKey="Macros"
                    isAnimationActive={false}
                    data={data}
                    cx={200}
                    cy={200}
                    outerRadius={80}
                    fill="#002db3"
                    labelLine={false}
                    label={renderCustomizedLabel}
                >
                {
                    data.map((entry, index) => <Cell key={`cell-${index}`} fill={COLORS[index % COLORS.length]} />)
                }
                </Pie>
                <Tooltip />
                </PieChart>
                <h3>Graph of weight Difference</h3>
                <LineChart width={300} height={100} data={weight_data}>
                    <Line type="monotone" dataKey="Weight" stroke="#8884d8" strokeWidth={2}  labelLine={true} lable/>
                </LineChart>
             </div>
        </div>
    );
}