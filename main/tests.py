import datetime
from django.contrib.auth.models import User, Group
from django.test import TestCase
from django.urls import reverse

from main.models import Competition, Education, Experience, Project


class MainTest(TestCase):
    def setUp(self):
        # Create standard test accounts
        self.owner = User.objects.create_superuser(
            username="owner", password="test-password", email="owner@example.com"
        )
        self.editor = User.objects.create_user(username="editor", password="test-password")
        self.editor_group = Group.objects.create(name="Editor")
        self.editor.groups.add(self.editor_group)
        self.user = User.objects.create_user(username="regularuser", password="test-password")

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
            duration="2025 – Present",
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
            duration="2023 – 2024",
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

        # Project entry
        self.project = Project.objects.create(
            title="Portfolio Website",
            description="Personal portfolio app in Django",
            tech_stack="Django, HTML, CSS",
            project_url="https://example.com",
        )

    # --- MODEL & PROPERTY TESTS ---

    def test_model_str_representations(self):
        self.assertEqual(str(self.edu1), "Ilmu Komputer KKI - Universitas Indonesia")
        self.assertEqual(str(self.exp1), "English Debate Society Universitas Indonesia (EDS UI)")
        self.assertEqual(str(self.comp1), "Freshman Cup 2026 - Co-9th Best Speaker")
        self.assertEqual(str(self.project), "Portfolio Website")

    def test_education_coursework_list_property(self):
        courses = self.edu1.coursework_list
        self.assertIn("Calculus 1 & 2", courses)
        self.assertIn("Data Structures & Algorithms", courses)
        self.assertEqual(len(courses), 6)

        # Test empty coursework fallback
        empty_edu = Education.objects.create(degree="Test", institution="Test")
        self.assertEqual(empty_edu.coursework_list, [])

    def test_experience_skills_list_and_ongoing_property(self):
        skills = self.exp1.skills_list
        self.assertIn("Organization", skills)
        self.assertIn("Recruitment", skills)
        self.assertEqual(len(skills), 4)

        # Test is_ongoing logic
        self.assertTrue(self.exp1.is_ongoing)
        self.assertFalse(self.exp2.is_ongoing)
        self.assertTrue(self.exp3.is_ongoing)  # No duration specified defaults to ongoing

        # Test empty skills fallback
        empty_exp = Experience.objects.create(title="Test", description="Test")
        self.assertEqual(empty_exp.skills_list, [])

    def test_competition_tags_list_property(self):
        tags = self.comp1.tags_list
        self.assertIn("Debate", tags)
        self.assertIn("Public Speaking", tags)
        self.assertEqual(len(tags), 2)

        # Test empty tags fallback
        empty_comp = Competition.objects.create(title="Test", award="Test", date_str="2026")
        self.assertEqual(empty_comp.tags_list, [])

    # --- PAGE ACCESSIBILITY & TEMPLATE TESTS ---

    def test_main_url_is_accessible_and_has_context(self):
        response = self.client.get(reverse("main:show_main"))
        self.assertEqual(response.status_code, 200)
        self.assertTemplateUsed(response, "index.html")
        self.assertTemplateUsed(response, "base.html")
        self.assertIn("name", response.context)
        self.assertIn("bio", response.context)
        self.assertIn("npm", response.context)

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

    def test_projects_url_is_accessible(self):
        response = self.client.get(reverse("main:show_projects"))
        self.assertEqual(response.status_code, 200)
        self.assertTemplateUsed(response, "project.html")

    def test_navigation_links_present(self):
        response = self.client.get(reverse("main:show_main"))
        self.assertContains(response, f'href="{reverse("main:show_main")}"')
        self.assertContains(response, f'href="{reverse("main:show_experience")}"')
        self.assertContains(response, f'href="{reverse("main:show_competition")}"')
        self.assertContains(response, f'href="{reverse("main:show_education")}"')

    def test_nonexistent_page_returns_404(self):
        response = self.client.get("/a-page-that-does-not-exist/")
        self.assertEqual(response.status_code, 404)

    # --- AUTHENTICATION & COOKIE TESTS ---

    def test_user_registration(self):
        response = self.client.post(
            reverse("main:register"),
            {
                "username": "newuser",
                "password1": "ComplexPass123!",
                "password2": "ComplexPass123!",
            },
        )
        self.assertEqual(response.status_code, 302)
        self.assertTrue(User.objects.filter(username="newuser").exists())

    def test_login_logout_and_last_login_cookie(self):
        # 1. Login (follow=False inspects the 302 response where set_cookie was executed)
        response = self.client.post(
            reverse("main:login"),
            {"username": "regularuser", "password": "test-password"},
            follow=False,
        )
        self.assertEqual(response.status_code, 302)
        self.assertIn("last_login", response.cookies)

        # 2. Verify cookie on profile main view
        response_main = self.client.get(reverse("main:show_main"))
        self.assertNotEqual(
            response_main.context["last_login"],
            "No active login session / Cookie not found",
        )

        # 3. Logout
        response_logout = self.client.get(reverse("main:logout"))
        self.assertEqual(response_logout.status_code, 302)
        self.assertFalse("_auth_user_id" in self.client.session)

    # --- VIEW PERMISSION & UPDATE ROUTE TESTS ---

    def test_update_views_require_login_and_permission(self):
        update_url = reverse("main:update_experience", args=[self.exp1.id])
        
        # 1. Anonymous user redirected to login
        response = self.client.get(update_url)
        self.assertEqual(response.status_code, 302)

        # 2. Regular user gets 403 PermissionDenied
        self.client.force_login(self.user)
        response = self.client.get(update_url)
        self.assertEqual(response.status_code, 403)

        # 3. Editor user gets 200 OK
        self.client.force_login(self.editor)
        response = self.client.get(update_url)
        self.assertEqual(response.status_code, 200)

        # 4. Superuser gets 200 OK
        self.client.force_login(self.owner)
        response = self.client.get(update_url)
        self.assertEqual(response.status_code, 200)