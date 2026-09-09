# Personal Design Guide

토스(Toss)의 Product Principles를 참고하여 만든 나만의 디자인 가이드.
어떤 제품을 만들든 화면, 문구, 흐름을 결정할 때 이 문서를 기준으로 판단한다.

## 핵심 철학

> 좋은 UX는 사용자가 "생각하지 않아도 되는" 경험이다.
> 사용자가 지불하는 모든 비용(인지·심리·노동)을 줄이고,
> 비용을 요구하기 전에 얻을 가치를 먼저 보여준다.

## 구조

### 3대 원칙 (Core Principles)

| 원칙 | 한 줄 요약 | 문서 |
|------|-----------|------|
| 1. Simplicity | 배우지 않아도 본능적으로 이해할 수 있게 만든다 | [principles/01-simplicity.md](principles/01-simplicity.md) |
| 2. Easy to Answer | 사용자가 이미 알고 있는 것만 묻는다 | [principles/02-easy-to-answer.md](principles/02-easy-to-answer.md) |
| 3. Value First, Cost Later | 비용을 요구하기 전에 가치를 먼저 보여준다 | [principles/03-value-first.md](principles/03-value-first.md) |

### 운영 가이드 (원칙을 지속시키는 방법)

| 가이드 | 한 줄 요약 | 문서 |
|--------|-----------|------|
| UX Writing | 문구도 시스템으로 관리한다 | [guides/ux-writing.md](guides/ux-writing.md) |
| 시스템화 | 좋은 UX를 사람의 감각이 아닌 시스템에 맡긴다 | [guides/systemization.md](guides/systemization.md) |

### 실무 도구

| 도구 | 용도 | 문서 |
|------|------|------|
| 리뷰 체크리스트 | 화면/기능 출시 전 셀프 리뷰 | [checklists/review-checklist.md](checklists/review-checklist.md) |
| 디자인 시스템 | AI에게 UI 제작을 시킬 때 전달하는 구체적 스펙 (색·글꼴·간격·컴포넌트·톤) | [DESIGN_SYSTEM.md](DESIGN_SYSTEM.md) |
| 대비 검사 | 색 토큰을 바꾼 뒤 WCAG AA 통과 여부 검증 (`python scripts/check-contrast.py`) | [scripts/check-contrast.py](scripts/check-contrast.py) |

## 사용 방법

1. **새 화면을 설계할 때** — 3대 원칙 문서를 순서대로 훑으며 설계를 점검한다.
2. **문구를 쓸 때** — [ux-writing.md](guides/ux-writing.md)의 규칙과 템플릿을 따른다.
3. **출시 직전** — [review-checklist.md](checklists/review-checklist.md)로 최종 점검한다.
4. **같은 문제를 두 번 발견하면** — 개별 수정에 그치지 말고 [systemization.md](guides/systemization.md)에 따라 가이드/컴포넌트로 승격시킨다.

## 출처

- 토스가 공식적으로 밝힌 Product Principle: **Simplicity**, **Easy to Answer**, **Value First, Cost Later**
- 그 외 항목(시스템화, UX Writing 운영)은 토스의 공개 사례에서 확인되는 운영 방식을 참고해 재구성한 것
- 참고 자료: [Toss Tech 블로그](https://toss.tech)
