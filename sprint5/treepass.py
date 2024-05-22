from __future__ import annotations
from typing import Optional


class Spaceman:

    def __init__(
            self,
            name: str,
            space_experience: int,
            father: Optional[Spaceman] = None,
            mother: Optional[Spaceman] = None,
    ):
        self.name = name
        self.space_experience = space_experience
        self.father = father
        self.mother = mother


class DynastyExperienceCounter:

    def __init__(self, spaceman: Spaceman):
        self.root = spaceman
        self.total_experience: int = 0

    def count_dynasty_experience(self):
        # Доработайте метод, чтобы он считал
        # суммарный опыт династии космонавтов.
        self.total_experience += self.root.space_experience
        if self.root.father:
            f = DynastyExperienceCounter(self.root.father)
            self.total_experience += f.count_dynasty_experience()
        if self.root.mother:
            m = DynastyExperienceCounter(self.root.mother)
            self.total_experience += m.count_dynasty_experience()
        return self.total_experience


yu_a_makarin = Spaceman(
    name='Юрий Алексеевич Макарин',
    space_experience=10,
    father=Spaceman(
        name='Алексей Михайлович Макарин',
        space_experience=25,
        mother=Spaceman(
            name='Евгения Владимировна Беляева',
            space_experience=1
        )
    ),
    mother=Spaceman('Ангелина Васильевна Черенкова', 5)
)
counter = DynastyExperienceCounter(yu_a_makarin)
result = counter.count_dynasty_experience()
print(result)
