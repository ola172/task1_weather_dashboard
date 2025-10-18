# Weather Dashboard Website – Project Implementation Documentation

## Table of Contents
- [Project Overview](#project-overview)
- [Task Analysis & Implementation](#task-analysis--implementation)
- [Prompt Engineering & Documentation Support](#prompt-engineering--documentation-support)

---

## Project Overview
Weather Dashboard Website is a responsive web app providing real-time weather data via automatic geolocation or manual city input. Backend uses FastAPI with clean service separation, caching, and OpenWeatherMap integration; frontend uses Jinja2 templates and vanilla JavaScript for dynamic UI.

---

## Task Analysis & Implementation
Task implementation has been done on two main steps 
- **Features Extracted:**
  - Automatic geolocation detection with fallback manual city input.
  - Current weather display (temperature, humidity, wind, clouds, visibility, sunrise/sunset, description, icon).
  - Error handling for API/network failures and rate limits.
  - TTL caching with last-updated display.
  - Clean separation: thin controllers, services handling logic.

- **Implementation Steps:**
    The implementation step has been done trough 5 steps:
    1. Step-by-step plan defined: backend services → frontend → integration → testing.
    2. Choose the suitable technologies used for each part.
    3. Define the project structure before any implementation.
    4. Start implementation step by step with testing after each step.
    5. Finally, generate the detailed documentation for implemented task.

---

## Prompt Engineering & Documentation Support
- Through this task i have used LLM for for several parts:
    - Enhance prompts: 
        - To enhance prompts for ensuring best results, i have define a schema for enhanced prompts (**Role / Context:** - **Goal / Objective:** - **Inputs:** - **Instructions:**  - **Output Requirements:** - **Constraints / Notes:**  - **Example Output:**)
        - prompt:

            ```
            **Role:**
            You are an expert Prompt Engineer specializing in technical domains. Your mission is to enhance and professionalize prompts so they produce accurate, detailed, consistent, and high-quality outputs.

            **Input:**

            You will be provided with the following:

                1. Task Details: Description of the task that the enhanced prompt should accomplish.

                2. Original Prompt: The existing or draft prompt that needs improvement.

            **Your Objectives:**

            Refine and expand the original prompt to ensure:

                - Clarity: Clear intent, unambiguous instructions.

                - Completeness: Includes all necessary context, constraints, and goals.

                - Professional Tone: Uses formal, instructive, and domain-appropriate language.

                - Technical Precision: Correct terminology and logical structure for technical tasks.

                - Consistency: Matches the unified structure described below.

            **Output Format (Unified Prompt Structure):**
                strictly follow this structure:
                ```
                ### Enhanced Prompt

                **Role / Context:**  
                [Define the role or identity the model should assume, e.g., "You are a senior Python developer specializing in data pipelines."]

                **Goal / Objective:**  
                [Clearly state what the prompt is intended to achieve.]

                **Inputs:**  
                [List the inputs or parameters expected from the user or system.]

                **Instructions:**  
                [Provide step-by-step guidance or criteria for completing the task.]

                **Output Requirements:**  
                [Describe what the ideal output should look like—format, tone, level of detail, etc.]

                **Constraints / Notes:**  
                [Specify any limitations, rules, or quality guidelines to follow.]


                **Example Output:**

                (Only if examples are requested; otherwise, omit.)
                ```
            ```

    - Planning: 

        - suggest the step by step plan to work on through implementation and help in choosing suitable technologies for each stack in task

        - prompt:

        ```
        **Role / Context:**  
        You are a senior full-stack software architect specializing in Python web development using FastAPI and modern frontend technologies. You are experienced in designing end-to-end architectures for scalable, user-friendly web applications. Your responsibility is to produce a **complete, structured implementation plan** (not code) for the Weather Dashboard Website project.

        **Goal / Objective:**  
        Develop a detailed, professional, and technically justified **implementation plan** for building a Weather Dashboard Website. The plan should describe every major phase of development — backend, frontend, integration, testing, and deployment — ensuring the result is a responsive, reliable, and visually appealing weather application.

        **Inputs:**  
        - Task name: Weather Dashboard Website  
        - Requirements:  
        - Detect user location  
        - Fallback option for manual city input if location detection fails  
        - Fetch current weather data from a free API (e.g., OpenWeatherMap, WeatherAPI)  
        - Display weather details: temperature, humidity, wind speed, weather description  
        - Handle common errors gracefully (e.g., network issues, API failures, location detection errors)  
        - Provide visually appealing and user-friendly interface  
        - Run on localhost with a Python backend framework (FastAPI preferred)  
        - Include additional helpful or creative features if relevant  

        **Instructions:**  
        1. **Backend Architecture:**  
        - Define the structure of the FastAPI backend, including routes, services, and models.  
        - define all routes to implement based on the feature required in task
        - Describe the process for integrating with a weather API and managing API keys securely.  
        - Explain how user location detection and fallback city input should be implemented.  
        - Include handling for API rate limits, request caching, and data validation.  

        2. **Frontend Development:**  
        - Outline the frontend technology stack (e.g., HTML, CSS, JS, or frameworks like React/Vue).  
        - Explain how the frontend interacts with the backend to fetch and display data dynamically.  
        - Include plans for responsive layout, accessibility, and visual styling (modern, clean design).  
        - Describe how user inputs and feedback (e.g., error messages, loading states) are handled.  

        3. **Testing and Validation:**  
        - Define test strategies for each layer: backend API testing, frontend functional testing, and integration testing.  
        - Include approaches for testing error handling, input validation, and location detection.  
        - Describe UX validation methods to ensure clarity and responsiveness.  

        4. **Non-Functional Considerations:**  
        - Address maintainability, scalability, and security aspects.  
        - Include performance optimizations (e.g., caching, async requests).  
        - Outline potential deployment path (localhost → production-ready setup).  

        5. **Technology Recommendations:**  
        - For each component (backend, frontend, data fetching, UI), list suitable frameworks or libraries.  
        - Justify each choice in terms of **performance**, **simplicity**, **scalability**, and **developer experience**.  
        - my preferences is FastAPI and jinja2 , take my preferences in consideration while recommending suitable technologies

        6. **Implementation Flow:**  
        - Present the full plan as a logically ordered roadmap (e.g., Step 1 → Step 2 → Step 3 …).  
        - Each step should be clear, actionable, and directly linked to the final functional outcome.  
        
        7. consider to avoid any complexity as this task is assessment task not production product.
        8. cosider the isolation between backend-logic and front-end logic in implementation and in project structure.

        **Output Requirements:**  
        - A **structured, multi-section document** detailing the entire implementation plan.  
        - Each section must include sub-points, technical explanations, and justifications.  
        - The tone should be professional, instructive, and concise — suitable for technical documentation.  
        - Exclude all code snippets or pseudo-code.  
        - The final plan should be easily understandable by both backend and frontend developers.
        **Constraints / Notes:**  
        - Focus exclusively on planning, architecture, and rationale — do **not** generate any implementation code.  
        - Use domain-appropriate technical terminology and maintain logical consistency across sections.  
        - Ensure clarity, readability, and completeness suitable for project kick-off documentation.
        ```
    
    - Implementation process: 
        - after defining the detailed plan to go through, i walk through conversation to implement each step.
        - sometimes, i made manual changes to codebase like (configuration, custom exceptions, enhancing UI).
        - conversation link: https://chatgpt.com/share/68f2ef61-d720-8002-b9d3-bde4f20a8b11
    