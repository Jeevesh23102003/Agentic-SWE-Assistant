# FILE STRUCTURE

- **agent.py**: It contains all the agents and their codes.

- **agent_store.py**: Contains code for the agent selection process.

- **Requirements.txt**: Contains all dependencies needed to be installed.
  
- **custom_generate.py**: Contains code for a custom generate function required at many places in our codebase.
  
- **filter.py**: Contains code for the tasks of context filtering.

- **complexity_evaluator.py**: Contains code for evaluating the complexity of a query and determining the class in which this query belongs.

- **database.py**: Initializes rag client using PATHWAY.

- **rag_server.py**: Initializes a pathway vector server.

- **rag_client.py**: Client for pathway vector server.

- **app.py**: Streamlitt front of our UI application.

- **memory.py**: Contains code for short and core memory.

- **prompts.py**: Contains all prompt templates required.

- **query_decomposer.py**: Contains code for breaking complex multi-hop queries to simple single-hop sub-queries.

- **variables.py**: Fill your API keys here.

- **main.py**: It contains the main code in which all the other classes and functions are called for the required project purpose.