# # agent.py
# import json
# import time
# from groq_client import stream_completion, get_completion
# from output_formatter import type_out_text, print_panel
# from rich.console import Console

# console = Console()

# class WorkerAgent:
#     def __init__(self, role, task_description):
#         self.role = role
#         self.task_description = task_description

#     def execute(self, user_query):
#         messages = [
#             {"role": "system", "content": f"You are a {self.role} agent specializing in {self.task_description}."},
#             {"role": "user", "content": f"Problem: {user_query}\nPlease perform your task."}
#         ]
#         result = ""
#         for chunk in stream_completion(messages):
#             result += chunk
#             type_out_text(chunk)
#         return result

# class ManagerAgent:
#     def __init__(self):
#         self.console = console

#     def analyze_query(self, user_query):
#         system_message = (
#             # "You are a hierarchical reasoning agent. "
#             # "Based on the following problem input, dynamically determine the necessary hierarchical layers. "
#             # "Return a JSON list where each element is an object with 'layer' (name), 'role', and 'task'. "
#             # "For example: "
#             # "[ {\"layer\": \"Layer 1\", \"role\": \"Soldiers\", \"task\": \"Evidence Analysis\"}, "
#             # "{\"layer\": \"Layer 2\", \"role\": \"Officers\", \"task\": \"Legal Precedent Evaluation\"}, "
#             # "{\"layer\": \"Layer 3\", \"role\": \"General\", \"task\": \"Case Strategy Formulation\"} ]"
#             "You are a Hierarchical Reasoning Agent. Organize your reasoning into dynamic hierarchical layers where each layer has a specific role. "
#                 "Your output must exactly follow the format below, without any extra commentary:\n\n"
#                 "Step 1: Hierarchical Layer Creation\n"
#                 "- Created Layer 1: Evidence Analysis (Soldiers).\n"
#                 "- Created Layer 2: Legal Precedent Evaluation (Officers).\n"
#                 "- Created Layer 3: Case Strategy Formulation (General).\n\n"
#                 "Step 2: Task Delegation\n"
#                 "- Layer 1: Analyze all available evidence (e.g., documents, emails, patents).\n"
#                 "- Layer 2: Evaluate relevant legal precedents and case law.\n"
#                 "- Layer 3: Formulate a high-level case strategy based on the findings from Layers 1 and 2.\n\n"
#                 "Step 3: Layer Execution\n"
#                 "- Layer 1: Analyzing evidence...\n"
#                 "  - Findings: Key evidence includes emails discussing the disputed technology and patent filings.\n"
#                 "- Layer 2: Evaluating legal precedents...\n"
#                 "  - Findings: Precedents suggest that proving intent is critical in IP theft cases.\n"
#                 "- Layer 3: Formulating case strategy...\n"
#                 "  - Findings: Focus on disproving intent and highlighting the client's independent development of the technology.\n\n"
#                 "Step 4: Result Synthesis\n"
#                 "- Case Strategy:\n"
#                 "  1. Disprove intent by presenting evidence of independent development.\n"
#                 "  2. Highlight inconsistencies in the plaintiff's claims.\n"
#                 "  3. Use precedents to argue that the client's actions do not constitute IP theft.\n\n"
#                 "Do not include any additional information or commentary. Now, process the following problem input accordingly."
#         )
#         messages = [
#             {"role": "system", "content": system_message},
#             {"role": "user", "content": user_query}
#         ]
#         plan_response = get_completion(messages)
#         try:
#             layers = json.loads(plan_response)
#         except Exception as e:
#             # Fallback default layers in case of JSON parse error
#             layers = [
#                 {"layer": "Layer 1", "role": "Soldiers", "task": "Detail Analysis"},
#                 {"layer": "Layer 2", "role": "Officers", "task": "Intermediate Evaluation"},
#                 {"layer": "Layer 3", "role": "General", "task": "Final Synthesis"}
#             ]
#         return layers

#     def execute(self, user_query):
#         print_panel("Starting Hierarchical Reasoning", title="Agent", style="bold cyan")

#         # Step 1: Hierarchical Layer Creation
#         layers = self.analyze_query(user_query)
#         print_panel("Step 1: Hierarchical Layer Creation", title="Agent", style="bold green")
#         for layer in layers:
#             self.console.print(f"- Created {layer['layer']}: {layer['task']} ({layer['role']}).", style="cyan")
        
#         # Step 2: Task Delegation
#         print_panel("Step 2: Task Delegation", title="Agent", style="bold green")
#         for layer in layers:
#             self.console.print(f"- {layer['layer']} ({layer['role']}): {layer['task']} for input.", style="cyan")
        
#         # Step 3: Layer Execution
#         print_panel("Step 3: Layer Execution", title="Agent", style="bold green")
#         results = {}
#         for layer in layers:
#             self.console.print(f"- {layer['layer']}: Executing task: {layer['task']}...", style="magenta")
#             worker = WorkerAgent(layer['role'], layer['task'])
#             result = worker.execute(user_query)
#             results[layer['layer']] = result
#             self.console.print(f"\n  - Findings: {result}\n", style="magenta")
        
#         # Step 4: Result Synthesis
#         print_panel("Step 4: Result Synthesis", title="Agent", style="bold green")
#         synthesis_input = "Synthesize the following findings into a coherent final answer:\n"
#         for layer in layers:
#             synthesis_input += f"{layer['layer']} findings: {results[layer['layer']]}\n"
#         synthesis_input += "Provide a final, comprehensive answer."
#         messages = [
#             {"role": "system", "content": "You are a senior strategist synthesizing findings from multiple analyses."},
#             {"role": "user", "content": synthesis_input}
#         ]
#         final_answer = ""
#         for chunk in stream_completion(messages):
#             final_answer += chunk
#             type_out_text(chunk)
#         print_panel(final_answer, title="Final Answer", style="bold magenta")
#         return final_answer

#     def execute_streamlit(self, user_query, update_callback):
#         # Build up a full output string to update the Streamlit UI progressively.
#         full_text = ""
#         full_text += "## Welcome to the Hierarchical Reasoning Agent\n\n"
#         update_callback(full_text)
        
#         # Step 1: Hierarchical Layer Creation
#         layers = self.analyze_query(user_query)
#         full_text += "### Step 1: Hierarchical Layer Creation\n"
#         for layer in layers:
#             full_text += f"- Created {layer['layer']}: {layer['task']} ({layer['role']}).\n"
#         update_callback(full_text)
        
#         # Step 2: Task Delegation
#         full_text += "\n### Step 2: Task Delegation\n"
#         for layer in layers:
#             full_text += f"- {layer['layer']} ({layer['role']}): {layer['task']} for input.\n"
#         update_callback(full_text)
        
#         # Step 3: Layer Execution
#         full_text += "\n### Step 3: Layer Execution\n"
#         results = {}
#         for layer in layers:
#             full_text += f"- {layer['layer']}: Executing task: {layer['task']}...\n"
#             update_callback(full_text)
#             worker = WorkerAgent(layer['role'], layer['task'])
#             result = ""
#             # Execute worker task and update progressively
#             for chunk in stream_completion([
#                 {"role": "system", "content": f"You are a {layer['role']} agent specializing in {layer['task']}."},
#                 {"role": "user", "content": f"Problem: {user_query}\nPlease perform your task."}
#             ]):
#                 result += chunk
#                 full_text += chunk
#                 update_callback(full_text)
#                 time.sleep(0.02)
#             results[layer['layer']] = result
#             full_text += f"\n  - Findings: {result}\n"
#             update_callback(full_text)
        
#         # Step 4: Result Synthesis
#         full_text += "\n### Step 4: Result Synthesis\n"
#         synthesis_input = "Synthesize the following findings into a coherent final answer:\n"
#         for layer in layers:
#             synthesis_input += f"{layer['layer']} findings: {results[layer['layer']]}\n"
#         synthesis_input += "Provide a final, comprehensive answer."
#         messages = [
#             {"role": "system", "content": "You are a senior strategist synthesizing findings from multiple analyses."},
#             {"role": "user", "content": synthesis_input}
#         ]
#         full_text += "Synthesizing final answer...\n"
#         update_callback(full_text)
#         final_answer = ""
#         for chunk in stream_completion(messages):
#             final_answer += chunk
#             full_text += chunk
#             update_callback(full_text)
#             time.sleep(0.05)
#         full_text += "\n\n**Final Answer:**\n" + final_answer
#         update_callback(full_text)
#         return final_answer

import json
import time
from groq_client import stream_completion, get_completion
from output_formatter import type_out_text, print_panel
from rich.console import Console

console = Console()

class WorkerAgent:
    def __init__(self, role, task_description):
        self.role = role
        self.task_description = task_description

    def execute(self, user_query):
        messages = [
            {"role": "system", "content": f"You are a {self.role} agent specializing in {self.task_description}. Give only 1 finding for each layer."},
            {"role": "user", "content": f"Problem: {user_query}\nPlease perform your task."}
        ]
        result = ""
        for chunk in stream_completion(messages):
            result += chunk
            type_out_text(chunk)
        return result

class ManagerAgent:
    def __init__(self):
        self.console = console

    def analyze_query(self, user_query):
        # Prompt the LLM to generate dynamic layers (Step 1) in valid JSON format.
        system_message = (
            "You are a Hierarchical Reasoning Agent. Based on the problem input provided, "
            "dynamically generate the necessary hierarchical layers. Return a JSON object with a key 'step1' whose value is a list of objects. "
            "Each object must have the keys 'layer', 'role', and 'task'. The output must be valid JSON and follow this example exactly:\n\n"
            '{\n'
            '  "step1": [\n'
            '    {"layer": "Layer 1", "role": "Soldiers", "task": "Evidence Analysis"},\n'
            '    {"layer": "Layer 2", "role": "Officers", "task": "Legal Precedent Evaluation"},\n'
            '    {"layer": "Layer 3", "role": "General", "task": "Case Strategy Formulation"}\n'
            '  ]\n'
            '}\n\n'
            "Do not include any extra commentary. Now, process the following problem input accordingly."
        )
        messages = [
            {"role": "system", "content": system_message},
            {"role": "user", "content": user_query}
        ]
        plan_response = get_completion(messages)
        try:
            data = json.loads(plan_response)
            layers = data.get("step1", [])
        except Exception as e:
            # Fallback default layers in case of JSON parse error
            layers = [
                {"layer": "Layer 1", "role": "Soldiers", "task": "Detail Analysis"},
                {"layer": "Layer 2", "role": "Officers", "task": "Intermediate Evaluation"},
                {"layer": "Layer 3", "role": "General", "task": "Final Synthesis"}
            ]
        return layers

    def delegate_tasks(self, layers, user_query):
        # Prompt the LLM to dynamically generate task delegation instructions (Step 2) in valid JSON format.
        message_content = (
            "Based on the following problem input and hierarchical layers, provide task delegation instructions for each layer. "
            "Return a JSON object with a key 'step2' whose value is a list of objects. Each object must have the keys 'layer' and 'instruction'.\n\n"
            f"Problem Input: {user_query}\n"
            f"Hierarchical Layers: {json.dumps(layers)}\n\n"
            "For example, a valid response is:\n\n"
            '{\n'
            '  "step2": [\n'
            '    {"layer": "Layer 1", "instruction": "Analyze all available evidence (e.g., documents, emails, patents)."},\n'
            '    {"layer": "Layer 2", "instruction": "Evaluate relevant legal precedents and case law."},\n'
            '    {"layer": "Layer 3", "instruction": "Formulate a high-level case strategy based on the findings from Layers 1 and 2."}\n'
            '  ]\n'
            '}\n\n'
            "Do not include any additional commentary."
        )
        messages = [
            {"role": "system", "content": "You are an expert in hierarchical task delegation."},
            {"role": "user", "content": message_content}
        ]
        response = get_completion(messages)
        try:
            data = json.loads(response)
            instructions = data.get("step2", [])
        except Exception as e:
            # Fallback generic instructions per layer
            instructions = [
                {"layer": layer["layer"], "instruction": f"Perform {layer['task']} for the given problem."}
                for layer in layers
            ]
        return instructions

    def execute(self, user_query):
        print_panel("Starting Hierarchical Reasoning", title="Agent", style="bold cyan")

        # Step 1: Hierarchical Layer Creation (dynamic)
        layers = self.analyze_query(user_query)
        print_panel("Step 1: Hierarchical Layer Creation", title="Agent", style="bold green")
        for layer in layers:
            self.console.print(f"- Created {layer['layer']}: {layer['task']} ({layer['role']}).", style="cyan")
        
        # Step 2: Task Delegation (dynamic)
        print_panel("Step 2: Task Delegation", title="Agent", style="bold green")
        delegation_instructions = self.delegate_tasks(layers, user_query)
        for instruction in delegation_instructions:
            self.console.print(f"- {instruction['layer']}: {instruction['instruction']}", style="cyan")
        
        # Step 3: Layer Execution (dynamic based on sub-agent outputs)
        print_panel("Step 3: Layer Execution", title="Agent", style="bold green")
        results = {}
        for layer in layers:
            self.console.print(f"- {layer['layer']}: Executing task: {layer['task']}...", style="magenta")
            worker = WorkerAgent(layer['role'], layer['task'])
            result = worker.execute(user_query)
            results[layer['layer']] = result
            self.console.print(f"\n  - Findings: {result}\n", style="magenta")
        
        # Step 4: Result Synthesis (using dynamic findings)
        print_panel("Step 4: Result Synthesis", title="Agent", style="bold green")
        synthesis_input = "Synthesize the following findings into a coherent final answer:\n"
        for layer in layers:
            synthesis_input += f"{layer['layer']} findings: {results[layer['layer']]}\n"
        synthesis_input += "Provide a final, comprehensive answer."
        messages = [
            {"role": "system", "content": "You are a senior strategist synthesizing findings from multiple analyses. Finalize 3 bullet points based on analyses."},
            {"role": "user", "content": synthesis_input}
        ]
        final_answer = ""
        for chunk in stream_completion(messages):
            final_answer += chunk
            type_out_text(chunk)
        print_panel(final_answer, title="Final Answer", style="bold magenta")
        return final_answer

    def execute_streamlit(self, user_query, update_callback):
        # Build up a full output string to update the Streamlit UI progressively.
        full_text = ""
        full_text += "## Welcome to the Hierarchical Reasoning Agent\n\n"
        update_callback(full_text)
        
        # Step 1: Hierarchical Layer Creation
        layers = self.analyze_query(user_query)
        full_text += "### Step 1: Hierarchical Layer Creation\n"
        for layer in layers:
            full_text += f"- Created {layer['layer']}: {layer['task']} ({layer['role']}).\n"
        update_callback(full_text)
        
        # Step 2: Task Delegation
        full_text += "\n### Step 2: Task Delegation\n"
        delegation_instructions = self.delegate_tasks(layers, user_query)
        for instruction in delegation_instructions:
            full_text += f"- {instruction['layer']}: {instruction['instruction']}\n"
        update_callback(full_text)
        
        # Step 3: Layer Execution
        # full_text += "\n### Step 3: Layer Execution\n"
        # results = {}
        # for layer in layers:
        #     full_text += f"- {layer['layer']}: Executing task: {layer['task']}...\n"
        #     update_callback(full_text)
        #     worker = WorkerAgent(layer['role'], layer['task'])
        #     result = ""
        #     for chunk in stream_completion([
        #         {"role": "system", "content": f"You are a {layer['role']} agent specializing in {layer['task']}. Give only 1 finding for each layer."},
        #         {"role": "user", "content": f"Problem: {user_query}\nPlease perform your task."}
        #     ]):
        #         result += chunk
        #         full_text += chunk
        #         update_callback(full_text)
        #         time.sleep(0.02)
        #     results[layer['layer']] = result
        #     full_text += f"\n  - Findings: {result}\n"
        #     update_callback(full_text)
            # Within ManagerAgent.execute_streamlit(...)
        full_text += "\n### Step 3: Layer Execution\n"
        results = {}
        for layer in layers:
            full_text += f"- {layer['layer']}: Executing task: {layer['task']}...\n"
            update_callback(full_text)
            worker = WorkerAgent(layer['role'], layer['task'])
            result = ""
            # Stream the worker's response without duplicating it later.
            for chunk in stream_completion([
                {"role": "system", "content": f"You are a {layer['role']} agent specializing in {layer['task']}. Give only 1 finding for each layer."},
                {"role": "user", "content": f"Problem: {user_query}\nPlease perform your task."}
            ]):
                result += chunk
                # Update live without appending a separate findings line every time.
                update_callback(full_text + "  - Findings: " + result)
                time.sleep(0.02)
            results[layer['layer']] = result
            # Append the final findings line only once per layer.
            full_text += f"  - Findings: {result}\n"
            update_callback(full_text)

        
        # Step 4: Result Synthesis
        full_text += "\n### Step 4: Result Synthesis\n"
        synthesis_input = "Synthesize the following findings into a coherent final answer:\n"
        for layer in layers:
            synthesis_input += f"{layer['layer']} findings: {results[layer['layer']]}\n"
        synthesis_input += "Provide a final, comprehensive answer."
        messages = [
            {"role": "system", "content": "You are a senior strategist synthesizing findings from multiple analyses. Finalize 3 bullet points based on analyses."},
            {"role": "user", "content": synthesis_input}
        ]
        full_text += "Synthesizing final answer...\n"
        update_callback(full_text)
        final_answer = ""
        for chunk in stream_completion(messages):
            final_answer += chunk
            full_text += chunk
            update_callback(full_text)
            time.sleep(0.05)
        full_text += "\n\n**Final Answer:**\n" + final_answer
        update_callback(full_text)
        return final_answer
