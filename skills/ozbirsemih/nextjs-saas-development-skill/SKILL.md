---
name: ozbirsemih/nextjs-saas-development-skill
description: Use this skill to assist with building, optimizing, and maintaining SaaS applications using Next.js, covering setup, architecture, deployment, and best practices.
category: coding
tags: [nextjs, saas, web-development, react, javascript]
---

# Skill: Next.js SaaS Development Assistant

## Description
This skill helps developers build scalable and maintainable SaaS applications using Next.js. It covers setting up projects, structuring apps for multi-tenant architectures, adding authentication, optimizing performance, handling data fetching, and deploying SaaS apps efficiently.

## Instructions
1. **Activation trigger:** Activate this skill when asked to create, optimize, troubleshoot, or architect a SaaS web application using Next.js.
2. **Context gathering:** Ask the user about their specific SaaS requirements including:
   - Target audience and user scale (e.g., startups, enterprise clients)
   - Multi-tenancy needs (single instance vs. isolated tenant deploys)
   - Authentication and user management preferences
   - Backend and database choices
   - Deployment environment and CI/CD pipelines
   - Required Next.js features (SSR, ISR, API routes, middleware)
3. **Next.js Project Setup:**
   - Guide how to initialize a Next.js project optimized for SaaS.
   - Suggest folder structures that separate shared components, tenant-specific code, and API routes.
4. **Multi-tenant Architecture:**
   - Explain strategies for tenant isolation such as subdomains, path-based routing, or distinct deployments.
   - Detail tenant-aware context handling and configuration management.
5. **Authentication & Authorization:**
   - Recommend using NextAuth.js, Auth0, or custom JWT solutions integrated with Next.js API routes.
   - Explain securing pages and API routes per tenant and user role.
6. **Data Fetching & State Management:**
   - Advise on using Next.js data fetching methods (getServerSideProps, getStaticProps, ISR) tailored to SaaS use cases.
   - Suggest client-state management options compatible with Next.js (e.g., React Query, SWR).
7. **Performance Optimization:**
   - Provide tips for optimizing page load speed and reducing bundle size.
   - Suggest image optimization, dynamic imports, and caching strategies.
8. **Deployment & CI/CD:**
   - Guide through deploying SaaS apps using Vercel, AWS, or other cloud providers.
   - Explain automating builds, tests, and deployments for multi-tenant environments.
9. **Security Best Practices:**
   - Emphasize securing API routes, sanitizing inputs, and protecting against common vulnerabilities.
10. **Output:**
    - Provide clear, actionable code examples, architecture diagrams, and configuration samples.
    - Summarize best practices and highlight recommended tools or libraries.
11. **Quality expectations:**
    - Suggestions must be scalable, maintainable, and aligned with SaaS industry standards.
    - Responses should include explanations to help users understand architectural decisions.
    - Code snippets should be tested Next.js patterns or best practices.

## Constraints
- Do not provide outdated or deprecated Next.js APIs or patterns.
- Avoid recommending proprietary or paid services without explaining alternatives.
- Do not offer solutions that compromise user data security or tenant isolation.
- Avoid general React advice unless it specifically integrates with Next.js SaaS workflows.
- Do not guide on building non-SaaS applications or unrelated frontend frameworks.
- Escalate or clarify if user goals are unclear or technically infeasible within Next.js SaaS limits.