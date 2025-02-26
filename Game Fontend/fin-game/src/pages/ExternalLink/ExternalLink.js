import React from "react";
import "./KnowledgeBase.css";
import { financialTopics } from "..//..//dummyData";

export default function KnowledgeBase() {
    return (
        <div className="knowledge-container">
            <h1>Financial Literacy Knowledge Base</h1>
            <p>Explore various topics to enhance your financial literacy.</p>
            <div className="topics-grid">
                {financialTopics.map((topic, index) => (
                    <a 
                        key={index} 
                        className="topic-card" 
                        href={topic.link} 
                        target="_blank" 
                        rel="noopener noreferrer"
                    >
                        <h2>{topic.title}</h2>
                        <p>{topic.description}</p>
                        <div className="topic-footer">
                            <span>Views: {topic.views}</span>
                            <span>Contributors: {topic.contributors.join(", ")}</span>
                        </div>
                    </a>
                ))}
            </div>
        </div>
    );
}
