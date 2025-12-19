# EARS Notation Reference

EARS (Easy Approach to Requirements Syntax) provides structured patterns for writing unambiguous, testable requirements.

## Core Patterns

### Ubiquitous Requirements

Requirements that always apply, without specific conditions.

**Pattern:** `THE SYSTEM SHALL [action]`

**Examples:**
```
THE SYSTEM SHALL encrypt all stored passwords using bcrypt
THE SYSTEM SHALL log all authentication attempts
THE SYSTEM SHALL validate input before processing
```

### Event-Driven Requirements

Requirements triggered by a specific event.

**Pattern:** `WHEN [event] THE SYSTEM SHALL [response]`

**Examples:**
```
WHEN a user submits the login form THE SYSTEM SHALL validate credentials within 2 seconds
WHEN a file upload completes THE SYSTEM SHALL scan for malware before storing
WHEN the session expires THE SYSTEM SHALL redirect to the login page
```

### State-Driven Requirements

Requirements that apply while the system is in a particular state.

**Pattern:** `WHILE [state] THE SYSTEM SHALL [behavior]`

**Examples:**
```
WHILE in maintenance mode THE SYSTEM SHALL display a maintenance message to users
WHILE the database connection is unavailable THE SYSTEM SHALL queue writes for later processing
WHILE rate limited THE SYSTEM SHALL return HTTP 429 responses
```

### Conditional Requirements

Requirements dependent on a feature or configuration.

**Pattern:** `IF [condition] THEN THE SYSTEM SHALL [behavior]`

**Examples:**
```
IF two-factor authentication is enabled THEN THE SYSTEM SHALL require a verification code
IF the user has admin privileges THEN THE SYSTEM SHALL display the admin panel
IF debug mode is active THEN THE SYSTEM SHALL log detailed request information
```

### Optional Feature Requirements

Requirements for optional capabilities.

**Pattern:** `WHERE [feature] THE SYSTEM SHALL [behavior]`

**Examples:**
```
WHERE email notifications are configured THE SYSTEM SHALL send alerts for failed logins
WHERE API rate limiting is enabled THE SYSTEM SHALL track request counts per API key
WHERE audit logging is enabled THE SYSTEM SHALL record all data modifications
```

## Combining Patterns

Patterns can be combined for complex requirements:

```
WHILE the user is authenticated
WHEN they request to delete their account
IF they confirm the deletion
THEN THE SYSTEM SHALL schedule account deletion within 30 days
```

## Writing Good Requirements

### Be Specific and Testable

**Bad:** `THE SYSTEM SHALL be fast`

**Good:** `WHEN a user requests the dashboard THE SYSTEM SHALL render it within 500ms`

### One Requirement Per Statement

**Bad:** `THE SYSTEM SHALL validate email and send confirmation and log the event`

**Good:**
```
WHEN a user submits registration THE SYSTEM SHALL validate the email format
WHEN email validation succeeds THE SYSTEM SHALL send a confirmation email
WHEN a confirmation email is sent THE SYSTEM SHALL log the event
```

### Avoid Ambiguous Terms

Avoid: might, should, could, some, few, many, usually

Use: shall, must, will (for mandatory) + specific numbers

### Include Measurable Criteria

**Bad:** `THE SYSTEM SHALL handle high load`

**Good:** `THE SYSTEM SHALL support 1000 concurrent users with response times under 200ms`

## Success Criteria Checklist

Convert EARS requirements into testable acceptance criteria:

```markdown
## Success Criteria

WHEN a user submits valid credentials
THE SYSTEM SHALL authenticate them within 2 seconds

- [ ] Login with valid email/password succeeds
- [ ] Login completes in under 2 seconds under normal load
- [ ] Failed login attempts are logged
- [ ] Session token is returned on success
```

## Common Mistakes

### Vague Conditions

**Bad:** `WHEN something goes wrong THE SYSTEM SHALL handle it`

**Good:** `WHEN the database returns an error THE SYSTEM SHALL retry the operation up to 3 times before failing`

### Implementation Details in Requirements

**Bad:** `THE SYSTEM SHALL use Redis for caching`

**Good:** `THE SYSTEM SHALL cache frequently accessed data with a 5-minute TTL` (Redis is a design decision, not a requirement)

### Missing Edge Cases

Consider:
- What happens on failure?
- What happens with invalid input?
- What are the boundaries (min/max values)?
- What happens concurrently?
