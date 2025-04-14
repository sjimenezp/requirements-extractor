import dspy
import os

llm = dspy.LM(
    model="groq/llama3-8b-8192",
    api_key=os.getenv("GROQ_API_KEY"),
)
dspy.configure(lm=llm)


class RequirementsExtraction(dspy.Signature):
    """Extrae requerimientos estructurados de una transcripción de reunión."""

    transcript = dspy.InputField(
        desc="Transcripción de la reunión de levantamiento de requerimientos"
    )

    functional_requirements = dspy.OutputField(
        desc="Lista de requerimientos funcionales identificados"
    )
    non_functional_requirements = dspy.OutputField(
        desc="Lista de requerimientos no funcionales (rendimiento, seguridad, etc.)"
    )
    stakeholders = dspy.OutputField(
        desc="Personas interesadas mencionadas y sus roles/intereses"
    )
    action_items = dspy.OutputField(
        desc="Lista de elementos de acción acordados con responsables"
    )
    open_questions = dspy.OutputField(
        desc="Preguntas o temas que quedaron sin resolver"
    )
    constraints = dspy.OutputField(
        desc="Restricciones mencionadas (tiempo, presupuesto, tecnología)"
    )


class RequirementsExtractor(dspy.Module):
    def __init__(self):
        super().__init__()
        self.extract_requirements = dspy.ChainOfThought(RequirementsExtraction)

    def forward(self, transcript):
        return self.extract_requirements(transcript=transcript)


def analyze_meeting(transcript_path):
    with open(transcript_path, "r", encoding="UTF-8") as file:
        transcript = file.read()

    extractor = RequirementsExtractor()

    result = extractor(transcript)

    return result


if __name__ == "__main__":
    transcript_path = "transcripcion_reunion.txt"

    requirements_info = analyze_meeting(transcript_path)

    print("=== REQUERIMIENTOS FUNCIONALES ===")
    print(requirements_info.functional_requirements)

    print("\n=== REQUERIMIENTOS NO FUNCIONALES ===")
    print(requirements_info.non_functional_requirements)

    print("\n=== PERSONAS INTERESADAS ===")
    print(requirements_info.stakeholders)

    print("\n=== ELEMENTOS DE ACCIÓN ===")
    print(requirements_info.action_items)

    print("\n=== PREGUNTAS ABIERTAS ===")
    print(requirements_info.open_questions)

    print("\n=== RESTRICCIONES ===")
    print(requirements_info.constraints)
