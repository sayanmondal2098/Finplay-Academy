import React from "react";
import Topbar from "../../components/topbar/Topbar";
import Sidebar from "../../components/sidebar/sidebar";
import "./FinancialQuiz.css";
import QuizPage from "./QuizPage";



function FinancialQuiz() {
    return (

        <div className="App">
            <Topbar />
            <div className="container">
                <Sidebar />
                <div className="financialQuiz">
                    <QuizPage />
                </div>

            </div>
        </div>

    );

}

export default FinancialQuiz;
