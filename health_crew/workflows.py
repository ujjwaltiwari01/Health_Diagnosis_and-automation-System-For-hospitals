from crewai import Crew, Process
from .agents import (
    symptom_analyzer,
    history_reviewer,
    treatment_agent,
    referral_agent,
    interaction_checker,
    scheduler_agent,
    communication_agent,
    imaging_analyst,
)
from .tasks import (
    symptom_analysis_task,
    history_review_task,
    treatment_recommendation_task,
    referral_assessment_task,
    drug_safety_check_task,
    follow_up_scheduling_task,
    patient_communication_task,
    imaging_analysis_task,
)


def build_diagnosis_crew(verbose: bool = True, include_imaging: bool = False) -> Crew:
    """
    Build diagnosis crew with optional imaging analysis.
    
    Args:
        verbose: Enable verbose output
        include_imaging: Include imaging analysis agent and task
    """
    agents = [
        symptom_analyzer,
        history_reviewer,
        treatment_agent,
        referral_agent,
        interaction_checker,
        scheduler_agent,
        communication_agent,
    ]
    tasks = [
        symptom_analysis_task,
        history_review_task,
        treatment_recommendation_task,
        referral_assessment_task,
        drug_safety_check_task,
        follow_up_scheduling_task,
        patient_communication_task,
    ]
    
    # Add imaging analysis if requested and image provided
    if include_imaging:
        agents.insert(1, imaging_analyst)  # Add after symptom analyzer
        tasks.insert(1, imaging_analysis_task)  # Run imaging early for context
    
    crew = Crew(agents=agents, tasks=tasks, process=Process.sequential, verbose=verbose)
    return crew
