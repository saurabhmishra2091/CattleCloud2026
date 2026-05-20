# Extra detailed content for CattleCloud PDF (used by generate_pdf.py)


def expand_ch1(story, styles, body, h2, h3, bullet, sp, std_table, PAGE_W, MARGIN, PageBreak):
    story.append(h2("1.4 Organization of the Report", styles))
    story.append(body(
        'This document is structured to follow standard software engineering practice for academic '
        'minor projects. Chapters 1–3 establish context, survey, and objectives. Chapters 4–6 cover '
        'analysis, design, and technology choices. Chapters 7–9 describe implementation and database '
        'design. Chapters 10–13 address security, user interface, algorithms, and API specification. '
        'Chapters 14–16 present testing, deployment, and results. Chapters 17–19 discuss limitations, '
        'future work, and conclusion. Appendices provide directory structure, glossary, references, and '
        'viva preparation material.', styles))
    story.append(h2("1.6 Motivation for Digital Livestock Management", styles))
    for b in [
        'India produces over 200 million tonnes of milk annually, with a large share from smallholder farms.',
        'Government schemes promote animal tagging and veterinary outreach, but daily operational records remain farmer-managed.',
        'A simple web dashboard reduces dependency on memory during peak milking and feeding hours.',
        'Digital records can be shown to veterinarians or dairy cooperatives without re-typing information.',
        'Students gain hands-on experience with authentication, REST APIs, and document databases used in industry.',
    ]:
        story.append(bullet(b, styles))
    story.append(h2("1.7 Project Repository Structure", styles))
    story.append(body(
        'The monorepo contains three logical parts: <b>backend/</b> (Node.js API), '
        '<b>smart-livestock-dashboard/</b> (React client), and <b>data/</b> (JSON seed files from '
        'early prototyping, not used at runtime). Environment secrets live in backend/.env and must '
        'never be committed to public repositories.', styles))
    rows = [
        ["Folder", "Purpose"],
        ["backend/", "Express server, Mongoose models, JWT middleware"],
        ["smart-livestock-dashboard/", "Vite + React SPA, pages, components"],
        ["data/", "Sample Animals.json, Milk.json — reference only"],
    ]
    w = [(PAGE_W - 2 * MARGIN) * x for x in [0.3, 0.7]]
    story.append(std_table(rows, col_widths=w))


def expand_ch2(story, styles, body, h2, bullet, sp, std_table, PAGE_W, MARGIN):
    story.append(h2("2.5 Government and Cooperative Portals", styles))
    story.append(body(
        'Regional agriculture departments and milk cooperatives operate portals for subsidy registration, '
        'bulk milk collection, and scheme enrollment. These systems focus on institutional data rather than '
        'a private farm notebook. CattleCloud complements such platforms by giving each farmer a personal '
        'ledger for herd health and daily operations without replacing government workflows.', styles))
    story.append(h2("2.6 Technology Trends in Agri-Tech", styles))
    trends = [
        ["Trend", "Relevance to CattleCloud"],
        ["Cloud databases (MongoDB Atlas)", "Scalable persistence via MONGO_URI"],
        ["JWT for SPAs", "Matches React + Express architecture"],
        ["Bilingual rural UI", "English/Hindi via translations.js"],
        ["Data visualization", "Chart.js weekly milk bar chart"],
        ["PWA / offline", "Future enhancement for low connectivity"],
        ["IoT milk sensors", "Out of scope; manual entry in current version"],
    ]
    story.append(std_table(trends, col_widths=[(PAGE_W - 2 * MARGIN) * x for x in [0.35, 0.65]]))
    story.append(h2("2.7 Gap Analysis", styles))
    story.append(body(
        'Existing manual and spreadsheet methods fail to combine <b>authentication</b>, <b>per-user privacy</b>, '
        '<b>vaccination scheduling logic</b>, and <b>unified milk plus finance reporting</b> in one browser '
        'application. CattleCloud fills this gap for demonstration and farmer pilot use, while acknowledging '
        'that enterprise herd software offers deeper breeding genetics and inventory modules.', styles))


def expand_ch3(story, styles, body, h2, h3, bullet, std_table, PAGE_W, MARGIN):
    story.append(h2("3.5 Secondary Objectives", styles))
    rows = [
        ["ID", "Objective", "Status"],
        ["S1", "Department aggregate dashboard", "Placeholder only"],
        ["S2", "Email-based password reset", "Not implemented"],
        ["S3", "Production full-stack deploy", "Frontend Netlify config only"],
        ["S4", "Automated unit tests", "Not implemented"],
    ]
    story.append(std_table(rows, col_widths=[(PAGE_W - 2 * MARGIN) * x for x in [0.1, 0.45, 0.45]]))
    story.append(h2("3.6 Working Hypothesis", styles))
    story.append(body(
        'If farmers maintain digital records for milk and vaccinations, they will spend less time '
        'reconciling paper notes and can identify underperforming animals faster—assuming basic smartphone '
        'or shared-computer access and stable internet during data entry sessions.', styles))


def expand_ch4(story, styles, body, h2, h3, bullet, std_table, PAGE_W, MARGIN):
    story.append(h2("4.4 Stakeholder Analysis", styles))
    rows = [
        ["Stakeholder", "Interest", "Interaction"],
        ["Farmer", "Daily operations", "Primary user of all modules"],
        ["Veterinarian", "Health history", "Indirect — farmer shows records"],
        ["Dairy cooperative", "Milk volume", "Future API integration"],
        ["Project evaluator", "Code quality, demo", "Report and viva"],
        ["Developer team", "Learning MERN patterns", "Build and maintain code"],
    ]
    story.append(std_table(rows, col_widths=[(PAGE_W - 2 * MARGIN) * x for x in [0.22, 0.38, 0.4]]))
    story.append(h2("4.5 As-Is vs To-Be Workflow", styles))
    story.append(h3("As-Is (Manual)", styles))
    story.append(body(
        'Farmer writes in notebook → manual sums at month end → optional Excel copy → '
        'difficult to search historical vaccination dates.', styles))
    story.append(h3("To-Be (CattleCloud)", styles))
    story.append(body(
        'Farmer opens browser → logs in → enters data in forms → MongoDB stores records → '
        'dashboard aggregates KPIs and charts instantly → delete/search available per module.', styles))


def expand_ch5(story, styles, body, h2, h3, bullet, code_block):
    story.append(h2("5.4 Login Sequence (Narrative)", styles))
    steps = [
        'User submits email and password on Login page.',
        'React sends POST /api/auth/login with JSON body.',
        'Server finds User by email; bcrypt.compare validates password.',
        'Server signs JWT with { id: user._id }, expiry 1 day.',
        'Client stores token, user name, and auth flag in localStorage.',
        'React Router navigates to /farmer-dashboard.',
        'Dashboard fetch calls include Authorization: Bearer token header.',
    ]
    for i, s in enumerate(steps, 1):
        story.append(bullet(f"<b>Step {i}:</b> {s}", styles))
    story.append(h2("5.5 Component Hierarchy (Frontend)", styles))
    story.append(code_block([
        "App.jsx",
        " ├── Public routes: Landing, Login, Register, ForgotPassword",
        " └── PrivateRoute",
        "      └── Layout (Topbar, Sidebar, Footer)",
        "           ├── FarmerDashboard",
        "           ├── Animal, Milk, Vaccination, Expenses",
        "           └── DepartmentDashboard (static)",
    ], styles))


def expand_ch6(story, styles, body, h2, h3, bullet):
    story.append(h2("6.4 Why React?", styles))
    story.append(body(
        'React provides component reusability (Card, Layout, Profile), a large ecosystem, hooks for '
        'state and side effects, and industry adoption. React 19 with Vite offers fast development '
        'with hot module replacement during implementation.', styles))
    story.append(h2("6.5 Why MongoDB?", styles))
    story.append(body(
        'Farm records vary in shape (animals vs milk vs expenses). Document storage avoids rigid '
        'relational migrations during prototyping. Mongoose adds schema validation while preserving '
        'flexibility for fields like optional profile images stored as long strings.', styles))
    story.append(h2("6.6 Why Express?", styles))
    story.append(body(
        'Express is minimal, widely taught, and integrates cleanly with JWT middleware and Mongoose. '
        'Express 5 is used in this project for modern routing and middleware patterns aligned with '
        'current Node.js LTS releases.', styles))


def expand_ch7(story, styles, body, h2, h3, bullet, code_block, std_table, PAGE_W, MARGIN):
    story.append(h2("7.5 Sample Register Request/Response", styles))
    story.append(code_block([
        "POST /api/auth/register",
        "Content-Type: application/json",
        "",
        '{ "name": "Ramesh", "email": "ramesh@gmail.com", "password": "***" }',
        "",
        "Response: { \"message\": \"User registered\" }",
    ], styles))
    story.append(h2("7.6 Animal Create — Field Mapping", styles))
    rows = [
        ["JSON body key", "Mongoose field", "Notes"],
        ["id", "animalId", "Farmer-defined tag"],
        ["breed", "breed", "From dropdown"],
        ["age", "age", "String in schema"],
        ["gender", "gender", "Male/Female/Other"],
        ["cost", "cost", "Purchase price"],
        ["health", "health", "e.g. Healthy, Sick"],
        ["(auto)", "user", "Set from JWT req.user.id"],
    ]
    story.append(std_table(rows, col_widths=[(PAGE_W - 2 * MARGIN) * x for x in [0.25, 0.25, 0.5]]))
    story.append(h2("7.7 Error Handling Pattern", styles))
    story.append(body(
        'Route handlers use try/catch blocks. Errors return HTTP 500 with { message: error.message }. '
        'Login failures return 400 with user-friendly messages. Missing JWT returns 401 from protect middleware. '
        'There is no centralized error middleware; improvement for production would use Express error handler.', styles))


def expand_ch8(story, styles, body, h2, h3, bullet, std_table, PAGE_W, MARGIN):
    story.append(h2("8.5 Login Page Behavior", styles))
    story.append(body(
        'Login.jsx posts to http://localhost:5000/api/auth/login. On success it saves token, user name, '
        'and auth=true, then navigates to farmer-dashboard. Password visibility toggle uses local show state. '
        'Errors display in red below the email field.', styles))
    story.append(h2("8.6 Register Page Validation", styles))
    for b in [
        'Phone number must be exactly 10 digits (UI validation only; not sent to API).',
        'Email must end with @gmail.com (client-side rule).',
        'Name and password read from form placeholders.',
    ]:
        story.append(bullet(b, styles))
    story.append(h2("8.7 Internationalization", styles))
    story.append(body(
        'translations.js exports text.en and text.hi objects with 100+ keys for sidebar, dashboard, forms, '
        'and landing page. App.jsx holds lang state and persists to localStorage. Topbar toggles EN/HI. '
        'LanguageContext exists but is not correctly wired in main.jsx — language primarily flows via props.', styles))
    story.append(h2("8.8 Chart.js Dashboard Integration", styles))
    story.append(body(
        'FarmerDashboard registers CategoryScale, LinearScale, BarElement, Tooltip, Legend. '
        'Weekly milk data aggregates records by weekday into a 7-element array for the bar chart. '
        'Chart label uses translated milkProduction string.', styles))


def expand_ch9(story, styles, body, h2, h3, std_table, PAGE_W, MARGIN):
    story.append(h2("9.4 Milk Collection", styles))
    rows = [
        ["Field", "Type", "Description"],
        ["user", "ObjectId", "Owner reference"],
        ["animalId", "String", "Links to animal tag"],
        ["date", "String", "YYYY-MM-DD from date input"],
        ["quantity", "Number", "Litres"],
    ]
    story.append(std_table(rows, col_widths=[(PAGE_W - 2 * MARGIN) * x for x in [0.22, 0.18, 0.6]]))
    story.append(h2("9.5 Expense Collection", styles))
    rows = [
        ["Field", "Type", "Description"],
        ["user", "ObjectId", "Owner"],
        ["type", "String", "Expense or Profit"],
        ["category", "String", "Feed, Milk Sale, etc."],
        ["amount", "Number", "INR"],
        ["date", "String", "Transaction date"],
        ["description", "String", "Optional notes"],
    ]
    story.append(std_table(rows, col_widths=[(PAGE_W - 2 * MARGIN) * x for x in [0.22, 0.18, 0.6]]))
    story.append(h2("9.6 Sample Seed Data (data/ folder)", styles))
    story.append(body(
        'Animals.json contains 10 sample entries (Jersey, Gir, Sahiwal, etc.) with id A1–A10. '
        'These files supported early UI mockups before MongoDB integration. They are not imported by server.js.', styles))


def expand_ch10(story, styles, body, h2, bullet):
    story.append(h2("10.5 Authorization vs Authentication", styles))
    story.append(body(
        '<b>Authentication</b> (protect middleware) verifies the JWT and identifies the user. '
        '<b>Authorization</b> is enforced by querying only documents where user field equals req.user.id. '
        'There is no admin role or cross-tenant read in the current codebase.', styles))
    story.append(h2("10.6 Profile Image Considerations", styles))
    for b in [
        'Client limits upload to 2 MB before base64 encoding.',
        'Entire image stored in User.image string — simple but increases document size.',
        'Production should use S3, Cloudinary, or GridFS with URL reference only.',
    ]:
        story.append(bullet(b, styles))


def expand_ch11(story, styles, body, h2, h3, bullet, std_table, PAGE_W, MARGIN, PageBreak):
    story.append(h2("11.6 Login Page (/login)", styles))
    story.append(body(
        'Branded as CattleCloud with aquamarine accent styling. Fields: email (required), password with '
        'show/hide toggle. Links to forgot-password and register. No role selection; all users route to '
        'farmer-dashboard after login.', styles))
    story.append(h2("11.7 Register Page (/register)", styles))
    story.append(body(
        'Collects farmer name, email, phone, password. Client validates Gmail suffix and 10-digit phone. '
        'Submits only name, email, password to backend.', styles))
    story.append(h2("11.8 Forgot Password (/forgot-password)", styles))
    story.append(body(
        '<b>Important limitation:</b> This flow reads users from localStorage, not MongoDB. It generates '
        'a 6-digit code client-side and updates local user array. It does not work for real registered '
        'accounts unless users were duplicated into localStorage manually. Production requires email OTP API.', styles))
    story.append(h2("11.9 Milk Production Page (/milk)", styles))
    rows_milk = [
        ["Element", "Description"],
        ["Form", "Animal ID, date picker, quantity in litres"],
        ["Table", "Per-row income = quantity × Rs. 70"],
        ["Footer row", "Total litres and total income"],
        ["Below table", "Average milk per record"],
    ]
    story.append(std_table(rows_milk, col_widths=[(PAGE_W - 2 * MARGIN) * x for x in [0.25, 0.75]]))
    story.append(h2("11.10 Expense Categories Detail", styles))
    story.append(h3("Expense types", styles))
    for c in ["Feed", "Veterinary", "Labor", "Equipment", "Maintenance", "Breeding", "Animal Purchase"]:
        story.append(bullet(c, styles))
    story.append(h3("Profit types", styles))
    for c in ["Milk Sale", "Dairy Products", "Animal Sale", "Manure Sale", "Government Subsidy"]:
        story.append(bullet(c, styles))
    story.append(h2("11.11 Department Dashboard", styles))
    story.append(body(
        'Route /department-dashboard shows static cards: 120 farms, 3200 animals, 12000L milk. '
        'No sidebar link; not connected to backend aggregation APIs.', styles))
    story.append(h2("11.12 Profile & Topbar", styles))
    story.append(body(
        'Profile.jsx fetches /api/users/profile, shows dropdown with upload (max 2MB), logout. '
        'Topbar provides menu hover for sidebar, language toggle, dark mode on body class, Profile component.', styles))
    story.append(h2("11.13 Navigation Map", styles))
    nav = [
        ["/farmer-dashboard", "Dashboard KPIs and chart"],
        ["/animals", "Herd registry"],
        ["/milk", "Production log"],
        ["/vaccination", "Vaccines and reminders"],
        ["/expenses", "Farm accounting"],
    ]
    story.append(std_table([["Route", "Purpose"]] + nav, col_widths=[(PAGE_W - 2 * MARGIN) * x for x in [0.4, 0.6]]))


def expand_ch11b(story, styles, body, h2, h3, bullet, PageBreak):
    """Second page group for UI chapter — landing detail."""
    story.append(PageBreak())
    story.append(h2("11.14 Landing Page Sections (Detailed)", styles))
    landing = [
        ("Hero", "Title, bilingual tagline, Get Started → register, Watch Demo YouTube link, Explore Features scroll."),
        ("Stats", "Marketing metrics: farms registered, milk tracked, farmers served."),
        ("Trusted By", "Dairy, agriculture, milk producers, community labels."),
        ("Features", "Six cards: animal registration, vaccine tracking, milk production, breeding, vet support, expenses."),
        ("Dashboard preview", "Screenshot-style image from Unsplash."),
        ("Benefits", "Save time, increase milk, control expenses, access anywhere."),
        ("How it works", "Three step cards: register, add animals, track daily."),
        ("Testimonial", "Five-star quote and CTA buttons."),
        ("FAQ", "Two Q&A items about cost and data safety."),
        ("Final CTA", "Start free registration button."),
    ]
    for title, desc in landing:
        story.append(bullet(f"<b>{title}:</b> {desc}", styles))


def expand_ch12(story, styles, body, h2, bullet):
    story.append(h2("12.8 Top Animal Selection", styles))
    story.append(body(
        'Milk records are grouped by animalId in a hash map; entries sorted descending by total quantity; '
        'first entry displayed as top producer on dashboard.', styles))
    story.append(h2("12.9 Average Milk on Milk Page", styles))
    story.append(body(
        'avgMilk = totalMilk / (record count || 1). Displayed below table with two decimal places.', styles))


def expand_ch13(story, styles, body, h2, code_block):
    story.append(h2("13.2 Sample Login Response", styles))
    story.append(code_block([
        "{",
        '  "token": "eyJhbGciOiJIUzI1NiIsInR5cCI6IkpXVCJ9...",',
        '  "name": "Ramesh Kumar"',
        "}",
    ], styles))
    story.append(h2("13.3 Sample Milk POST Body", styles))
    story.append(code_block([
        '{ "animalId": "A101", "date": "2026-05-19", "quantity": 12 }',
    ], styles))


def expand_ch14(story, styles, body, h2, bullet, std_table, PAGE_W, MARGIN):
    story.append(h2("14.4 Test Environment", styles))
    rows = [
        ["Component", "Configuration"],
        ["OS", "Windows 10/11"],
        ["Browser", "Chrome / Edge latest"],
        ["Backend", "http://localhost:5000"],
        ["Frontend", "http://localhost:5173 (Vite)"],
        ["Database", "Local MongoDB or Atlas"],
    ]
    story.append(std_table(rows, col_widths=[(PAGE_W - 2 * MARGIN) * x for x in [0.3, 0.7]]))
    story.append(h2("14.5 Integration Test Flow (End-to-End)", styles))
    for b in [
        'Register → Login → Add animal A1 → Add milk 15L today → Dashboard shows updated today milk.',
        'Add FMD vaccination → Verify upcomingDate six months ahead.',
        'Add expense Rs.2000 feed → Add profit Rs.8000 milk sale → Net profit Rs.6000.',
        'Logout → Attempt /animals → Redirect to login.',
    ]:
        story.append(bullet(b, styles))


def expand_ch15(story, styles, body, h2, bullet):
    story.append(h2("15.4 Production Gap", styles))
    story.append(body(
        'Netlify-hosted frontend still calls localhost:5000 unless VITE_API_URL is introduced. '
        'Backend must be deployed separately with HTTPS and CORS restricted to the Netlify domain.', styles))
    story.append(h2("15.5 Backup Strategy", styles))
    story.append(body(
        'Enable MongoDB Atlas automated backups. Export collections before schema changes. '
        'Document restore procedure for viva demonstration recovery.', styles))


def expand_ch16(story, styles, body, h2, bullet):
    story.append(h2("16.4 Discussion", styles))
    story.append(body(
        'The project demonstrates digitization themes in agriculture while remaining achievable in one '
        'semester. Trade-offs favor development speed over enterprise patterns (DTO validation, repository '
        'layer, microservices). Chart-based feedback may encourage daily milk logging—a behavioral benefit '
        'beyond storage alone.', styles))
    story.append(h2("16.5 Learning Outcomes (Extended)", styles))
    for b in [
        'Design RESTful resources aligned with domain entities.',
        'Implement bcrypt and JWT in Node.js.',
        'Build protected routes in React Router v7.',
        'Use Mongoose schemas with ObjectId references.',
        'Configure SPA deployment with fallback redirects.',
        'Document limitations honestly for academic integrity.',
    ]:
        story.append(bullet(b, styles))


def expand_ch17(story, styles, body, h2, bullet):
    story.append(h2("17.3 Operational Limitations", styles))
    for b in [
        'Requires internet for API; no offline PWA cache.',
        'No automated backup UI for farmer-exported data.',
        'Milk price hardcoded — not regional or market-linked.',
        'No SMS/push for vaccine due dates.',
    ]:
        story.append(bullet(b, styles))
    story.append(h2("17.4 Ethical Considerations", styles))
    story.append(body(
        'Farmer data stored in cloud database — privacy policy and consent flow not included in app. '
        'Recommend terms of use before any public production launch.', styles))


def expand_ch18(story, styles, body, h2, bullet):
    story.append(h2("18.4 Integration Roadmap", styles))
    story.append(body(
        'Phase 1: stability fixes (main.jsx, API URL, logout token clear). Phase 2: department APIs and '
        'password reset. Phase 3: IoT and AI analytics. This phased approach matches typical startup MVP evolution.', styles))


def expand_ch19(story, styles, body, h2, bullet):
    story.append(h2("19.1 Summary of Deliverables", styles))
    for b in [
        'Working farmer portal with five data modules.',
        'REST API with six route groups and JWT protection.',
        'MongoDB persistence with five collections.',
        'Bilingual marketing and application UI.',
        'Netlify-ready frontend build configuration.',
        'This project report and generated PDF documentation.',
    ]:
        story.append(bullet(b, styles))


def expand_ch7b(story, styles, body, h2, h3, bullet, code_block, chapter_block, PageBreak):
    """Additional backend implementation detail."""
    story.append(PageBreak())
    story += chapter_block("Chapter 7 (continued) — Backend Details", styles)
    story.append(h2("7.8 Middleware Execution Order", styles))
    story.append(body(
        'For every protected request, Express applies cors() and express.json() globally first. '
        'The route-specific protect middleware runs before the async handler. If verification succeeds, '
        'req.user contains the decoded JWT payload (at minimum the user id). Handlers never trust '
        'client-supplied user ids in the body — ownership is always taken from the token.', styles))
    story.append(h2("7.9 Collection Names in MongoDB", styles))
    story.append(body(
        'Mongoose pluralizes model names by default: User becomes users, Animal becomes animals, '
        'Milk becomes milks, Vaccination becomes vaccinations, Expense becomes expenses. Compass or '
        'Atlas UI will show these collection names when inspecting the database after first save.', styles))
    story.append(h2("7.10 Recommended Production Middleware", styles))
    for b in [
        'express-rate-limit on /api/auth/login to reduce brute force.',
        'helmet() for secure HTTP headers.',
        'express-validator or Zod for request body schema validation.',
        'morgan("combined") for access logging.',
        'Centralized error handler returning consistent JSON error shape.',
    ]:
        story.append(bullet(b, styles))
    story.append(h2("7.11 Dead Code Warning", styles))
    story.append(body(
        'The file backend/controllers/authcontroller.js contains alternate register/login using '
        'hardcoded JWT secret "SECRET123" and a role field not present in the User schema. This file '
        'is not mounted in server.js. Remove or merge it before production to avoid confusion during '
        'security review or viva questions.', styles))


def expand_ch4b(story, styles, body, h2, bullet, std_table, PAGE_W, MARGIN, PageBreak):
    story.append(PageBreak())
    story.append(h2("4.6 Module-wise Requirement Traceability", styles))
    rows = [
        ["Module", "Functional reqs", "Primary API"],
        ["Auth", "FR-1.x", "/api/auth"],
        ["Animals", "FR-2.x", "/api/animals"],
        ["Milk", "FR-3.x", "/api/milk"],
        ["Vaccination", "FR-4.x", "/api/vaccinations"],
        ["Expenses", "FR-5.x", "/api/expenses"],
        ["Dashboard", "FR-6.x", "GET animals + milk"],
        ["Profile", "—", "/api/users"],
    ]
    story.append(std_table(rows, col_widths=[(PAGE_W - 2 * MARGIN) * x for x in [0.22, 0.28, 0.5]]))
    story.append(h2("4.7 Assumptions", styles))
    for b in [
        'Farmers have basic literacy and can use web forms.',
        'Internet is available at least once per day for sync.',
        'Animal IDs are unique per farmer (not globally).',
        'Milk price Rs. 70/L is acceptable for demo revenue estimates.',
        'Dates are entered in local calendar and stored as strings.',
    ]:
        story.append(bullet(b, styles))


def expand_ch11c(story, styles, body, h2, h3, bullet, std_table, PAGE_W, MARGIN):
    story.append(h2("11.15 UI Styling Approach", styles))
    story.append(body(
        'Global CSS classes in index.css and App.css define landing page hero, feature grids, tables '
        '(.styled-table, .form-grid), and layout (.main-content, .topbar-fixed). Many authenticated '
        'pages mix className with inline style objects for rapid iteration. Dark mode toggles a class '
        'on document.body from Topbar. Color palette uses greens for agriculture branding and light gray '
        'table row backgrounds for readability.', styles))
    story.append(h2("11.16 Known UI Gaps", styles))
    gaps = [
        ["Gap", "Impact"],
        ["Dashboard vaccines=[]", "Vaccination KPI cards always zero"],
        ["No edit buttons", "User must delete and re-add to fix mistakes"],
        ["Sidebar hover-only", "Poor mobile discoverability"],
        ["Hardcoded API URL", "Production build cannot reach backend"],
        ["Forgot password local", "Misleading for real users"],
    ]
    story.append(std_table(gaps, col_widths=[(PAGE_W - 2 * MARGIN) * x for x in [0.35, 0.65]]))


def expand_viva_extra(story, styles, body, h2, bullet, chapter_block, PageBreak):
    story.append(PageBreak())
    story += chapter_block("Appendix H — Extended Viva Questions", styles)
    qa = [
        ("What is MERN?", "MongoDB, Express, React, Node — our stack uses Vite instead of CRA for React."),
        ("Difference between SQL and MongoDB here?", "We use flexible documents; no JOINs; user field links ownership."),
        ("What is CORS?", "Browser security; server uses cors() to allow frontend origin in dev."),
        ("How is password stored?", "bcrypt hash only; never plain text in database."),
        ("What happens when JWT expires?", "API returns 401; frontend should redirect to login (improvement area)."),
        ("Explain Chart.js usage.", "Bar chart of weekly milk totals on farmer dashboard."),
        ("What is PrivateRoute?", "React Router wrapper checking localStorage auth flag."),
        ("Why Netlify redirects?", "SPA needs index.html fallback for client routes like /animals."),
    ]
    for q, a in qa:
        story.append(body(f"<b>Q: {q}</b>", styles))
        story.append(body(f"<b>A:</b> {a}", styles))


def expand_appendices(story, styles, body, h2, h3, bullet, std_table, code_block, PAGE_W, MARGIN, chapter_block, sp, PageBreak):
    story.append(PageBreak())
    story += chapter_block("Appendix E — Translation Module", styles)
    story.append(body(
        'File: smart-livestock-dashboard/src/utils/translations.js exports const text = { en: {...}, hi: {...} }.', styles))
    cats = [
        ["Category", "Example keys"],
        ["Sidebar", "dashboard, animals, milk, vaccination, expenses"],
        ["Dashboard", "totalAnimals, todayMilk, weeklyMilk, farmScore"],
        ["Animal", "animalManagement, searchAnimal, addAnimal"],
        ["Milk", "milkProductionTitle, milkQuantity, averageMilk"],
        ["Landing", "heroTitle1, keyFeatures, faq, ctaTitle"],
    ]
    story.append(std_table(cats, col_widths=[(PAGE_W - 2 * MARGIN) * x for x in [0.3, 0.7]]))
    story.append(h3("Usage pattern", styles))
    story.append(code_block([
        "const t = text[lang] || text['en'];",
        "return <h2>{t.animalManagement}</h2>;",
    ], styles))
    story.append(PageBreak())
    story += chapter_block("Appendix G — How to Run the Project", styles)
    steps = [
        'Install Node.js LTS and MongoDB.',
        'cd backend → create .env with MONGO_URI, JWT_SECRET, PORT=5000.',
        'npm install && npm start → verify GET / returns Backend running.',
        'cd smart-livestock-dashboard → npm install && npm run dev.',
        'Open browser URL from Vite (usually :5173) → register and login.',
    ]
    for i, s in enumerate(steps, 1):
        story.append(bullet(f"{i}. {s}", styles))
