from django.test import TestCase
from django.urls import reverse

from main.models import Competition, Education, Experience


class MainTest(TestCase):
    def setUp(self):
        # Education entries
        self.edu1 = Education.objects.create(
            degree="Ilmu Komputer KKI",
            institution="Universitas Indonesia",
            date_range="2025 – Present",
            description_header="Completed & Ongoing Coursework:",
            coursework=(
                "Calculus 1 & 2\nDiscrete Mathematics 1 & 2\nLinear Algebra\n"
                "Introduction to Digital Systems\nFoundation of Programming 1 & 2\n"
                "Data Structures & Algorithms"
            ),
            location="Depok, Indonesia",
        )
        self.edu2 = Education.objects.create(
            degree="International Baccalaureate Diploma / High School Diploma",
            institution="ACG School Jakarta",
            date_range="2023 – 2025",
            description_header="IBDP Coursework:",
            coursework=(
                "Computer Science HL\nPhysics HL\nDigital Society HL\n"
                "Mathematics AA SL\nEnglish Language & Literature SL\nFrench AB Initio"
            ),
            location="Jakarta, Indonesia",
        )

        # Experience entries
        self.exp1 = Experience.objects.create(
            title="English Debate Society Universitas Indonesia (EDS UI)",
            role="Internals Staff",
            description=(
                "As a member of the Internals division at EDS UI, I assist in managing"
                " and hosting various internal affairs and institutional events,"
                " including Member Recruitment and UKM Display."
            ),
            category="organization",
            skills="Organization, Event Management, Internal Affairs, Recruitment",
        )
        self.exp2 = Experience.objects.create(
            title="Orcas Swim Team",
            role="Team Captain (Unofficial)",
            description=(
                "Assisted head coaches with training sessions, mentorship, and"
                " auxiliary operational duties for the high school swim team."
            ),
            category="leadership",
            skills="Leadership, Coaching Support, Mentorship, Team Operations",
        )
        self.exp3 = Experience.objects.create(
            title="Gecko House",
            role="House Captain · ACG School Jakarta",
            description=(
                "Led Gecko House operations and coordinated house activities,"
                " ranging from sports events to trivia. During my tenure the Gecko House"
                " secured the annual House Cup victory for the first time in several"
                " years."
            ),
            category="leadership",
            skills="Leadership, Operations, Coordination, Strategic Planning",
        )

        # Competition entries
        self.comp1 = Competition.objects.create(
            title="Freshman Cup 2026",
            award="Co-9th Best Speaker",
            organizer="EDS UI",
            location="",
            date_str="2026",
            description=(
                "Awarded Co-9th Best Speaker individual rank at the Freshman Cup"
                " parliamentary debate tournament."
            ),
            tags="Debate, Public Speaking",
        )
        self.comp2 = Competition.objects.create(
            title="Newbies 2026",
            award="49th Speaker & 11th Team (Team UI C)",
            organizer="EDS UI",
            location="",
            date_str="2026",
            description=(
                "Represented Universitas Indonesia as part of Team UI C, placing 11th"
                " overall in team standings and 49th individual speaker rank."
            ),
            tags="Debate, Critical Thinking",
        )
        self.comp3 = Competition.objects.create(
            title="Pekan Ristek Game Jam 2025",
            award="1st Place Winner",
            organizer="",
            location="",
            date_str="2025",
            description=(
                "Awarded 1st Place as part of duo team MasterSlaveFlipFlop for"
                " developing the winning entry, Destructon OS."
            ),
            tags="Game Development",
        )
        self.comp4 = Competition.objects.create(
            title="The World Scholar’s Cup",
            award="Global Round Medalist",
            organizer="Seoul Round",
            location="",
            date_str="Jul 2024",
            description=(
                "3rd Place Gold Medal: History (Scholar’s Challenge)\n13th Place Gold"
                " Medal: Scholar’s Bowl\nSilver Medals: Individual Debate, Science &"
                " Technology, Special Area, and Overall Scholar’s Challenge"
            ),
            tags="Academic, Debate & Writing",
        )
        self.comp5 = Competition.objects.create(
            title="The World Scholar’s Cup",
            award="Regional Round Medalist",
            organizer="Jakarta Round",
            location="",
            date_str="May 2024",
            description=(
                "1st Place Gold Medal: History (Scholar’s Challenge)\nGold Medals:"
                " Scholar’s Bowl, Overall Scholar’s Challenge\nSilver Medals:"
                " Collaborative Writing, Social Science, and Science & Technology"
            ),
            tags="Academic, Debate & Writing",
        )
        self.comp6 = Competition.objects.create(
            title="The World Scholar’s Cup",
            award="Tournament of Champions Medalist",
            organizer="Yale University",
            location="",
            date_str="Nov 2023",
            description=(
                "Silver Medal: Scholar’s Bowl Category\nSilver Medal: Collaborative"
                " Writing Category"
            ),
            tags="Academic, Global Finals",
        )
        self.comp7 = Competition.objects.create(
            title="The World Scholar’s Cup",
            award="Global Senior Round Medalist",
            organizer="Bangkok Round",
            location="",
            date_str="Aug 2023",
            description=(
                "Gold Medal: Scholar’s Challenge Category\nSilver Medals: Team Debate"
                " & Scholar’s Bowl Category"
            ),
            tags="Academic, Debate & Writing",
        )
        self.comp8 = Competition.objects.create(
            title="The World Scholar’s Cup",
            award="Regional Round Medalist",
            organizer="Jakarta Round",
            location="",
            date_str="May 2023",
            description="Gold Medal: Scholar’s Bowl Category",
            tags="Academic",
        )

    
    # URL accessibility and Template Test
    
    def test_main_url_is_accessible(self):
        response = self.client.get(reverse("main:show_main"))
        self.assertEqual(response.status_code, 200)
        self.assertTemplateUsed(response, "index.html")
        self.assertTemplateUsed(response, "base.html")

    def test_experience_url_is_accessible(self):
        response = self.client.get(reverse("main:show_experience"))
        self.assertEqual(response.status_code, 200)
        self.assertTemplateUsed(response, "experience.html")
        self.assertTemplateUsed(response, "base.html")

    def test_competition_url_is_accessible(self):
        response = self.client.get(reverse("main:show_competition"))
        self.assertEqual(response.status_code, 200)
        self.assertTemplateUsed(response, "competition.html")
        self.assertTemplateUsed(response, "base.html")

    def test_education_url_is_accessible(self):
        response = self.client.get(reverse("main:show_education"))
        self.assertEqual(response.status_code, 200)
        self.assertTemplateUsed(response, "education.html")
        self.assertTemplateUsed(response, "base.html")

    def test_navigation_links_present(self):
        response = self.client.get(reverse("main:show_main"))
        self.assertContains(response, f'href="{reverse("main:show_main")}"')
        self.assertContains(response, f'href="{reverse("main:show_experience")}"')
        self.assertContains(response, f'href="{reverse("main:show_competition")}"')
        self.assertContains(response, f'href="{reverse("main:show_education")}"')

    def test_nonexistent_page_returns_404(self):
        response = self.client.get("/a-page-that-does-not-exist/")
        self.assertEqual(response.status_code, 404)

    # Scenario 2: Model data Test when non Empty

    def test_education_page_renders_model_data(self):
        response = self.client.get(reverse("main:show_education"))
        self.assertEqual(response.status_code, 200)
        self.assertContains(response, self.edu1.degree)
        self.assertContains(response, self.edu1.institution)
        self.assertContains(response, self.edu1.location)
        self.assertContains(response, self.edu2.degree)
        self.assertContains(response, self.edu2.institution)

    def test_experience_page_renders_model_data(self):
        response = self.client.get(reverse("main:show_experience"))
        self.assertEqual(response.status_code, 200)
        self.assertContains(response, self.exp1.title)
        self.assertContains(response, self.exp1.role)
        self.assertContains(response, self.exp2.title)
        self.assertContains(response, self.exp3.title)

    def test_competition_page_renders_model_data(self):
        response = self.client.get(reverse("main:show_competition"))
        self.assertEqual(response.status_code, 200)
        self.assertContains(response, self.comp1.title)
        self.assertContains(response, self.comp1.award)
        self.assertContains(response, self.comp3.title)
        self.assertContains(response, self.comp3.award)
        self.assertContains(response, self.comp4.organizer)

    # Empty state message Test
    def test_empty_education_page(self):
        Education.objects.all().delete()
        response = self.client.get(reverse("main:show_education"))
        self.assertEqual(response.status_code, 200)
        self.assertContains(response, "No education has been added yet.")

    def test_empty_experience_page(self):
        Experience.objects.all().delete()
        response = self.client.get(reverse("main:show_experience"))
        self.assertEqual(response.status_code, 200)
        self.assertContains(response, "No experience has been added yet.")

    def test_empty_competition_page(self):
        Competition.objects.all().delete()
        response = self.client.get(reverse("main:show_competition"))
        self.assertEqual(response.status_code, 200)
        self.assertContains(response, "No competitions have been added yet.")