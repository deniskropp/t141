-- T3: Database Schema for Autonomous LLM Simulator

-- Table to store simulation metadata
CREATE TABLE simulations (
    id INTEGER PRIMARY KEY AUTOINCREMENT,
    name TEXT NOT NULL,
    objective TEXT NOT NULL,
    start_time TIMESTAMP DEFAULT CURRENT_TIMESTAMP,
    end_time TIMESTAMP,
    status TEXT NOT NULL -- e.g., 'running', 'completed', 'failed'
);

-- Table to store agent states
CREATE TABLE agents (
    id INTEGER PRIMARY KEY AUTOINCREMENT,
    simulation_id INTEGER NOT NULL,
    name TEXT NOT NULL,
    state TEXT, -- Can be JSON to store complex state
    FOREIGN KEY (simulation_id) REFERENCES simulations (id)
);

-- Table to store tasks
CREATE TABLE tasks (
    id INTEGER PRIMARY KEY AUTOINCREMENT,
    simulation_id INTEGER NOT NULL,
    parent_task_id INTEGER,
    prompt TEXT NOT NULL,
    plan TEXT,
    status TEXT NOT NULL, -- e.g., 'pending', 'in_progress', 'completed', 'failed'
    result TEXT,
    creation_time TIMESTAMP DEFAULT CURRENT_TIMESTAMP,
    completion_time TIMESTAMP,
    FOREIGN KEY (simulation_id) REFERENCES simulations (id),
    FOREIGN KEY (parent_task_id) REFERENCES tasks (id)
);

-- Table to store logs
CREATE TABLE logs (
    id INTEGER PRIMARY KEY AUTOINCREMENT,
    simulation_id INTEGER NOT NULL,
    task_id INTEGER,
    timestamp TIMESTAMP DEFAULT CURRENT_TIMESTAMP,
    level TEXT NOT NULL, -- e.g., 'INFO', 'WARNING', 'ERROR'
    message TEXT NOT NULL,
    FOREIGN KEY (simulation_id) REFERENCES simulations (id),
    FOREIGN KEY (task_id) REFERENCES tasks (id)
);
