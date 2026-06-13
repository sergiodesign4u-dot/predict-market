# Jobs To Be Done — Prediction Market Platform

> Format: Когда [ситуация] → я хочу [мотивация] → чтобы [результат]
> Rule: no product feature names in formulations — only human progress.
> Source discipline: each job cites persona + research origin. Jobs without data → Hypotheses section only.
> Built from: personas.md · master-research.md · CLAUDE.md · ux-patterns.md · aarrr.md · benchmark-trust.md · live-research F1–F3

---

## Как читать этот документ

```
MJ   — Main Job (1): job of the whole product
FJ1–FJ5 — Functional Jobs: steps on the path to MJ
EJ1–EJ3 — Emotional Jobs: how the person wants to feel
SJ1–SJ2 — Social Jobs: what they want others to see
HJ1–HJ4 — Hypotheses: jobs not backed by data — not in main list
```

**Hierarchy:** MJ → FJ (necessary steps) → EJ + SJ (layer on top of every step).
A person can fail at FJ2 and never reach MJ. EJ and SJ don't depend on each other.

---

## MJ · Main Job

### MJ — Когда событие, за которым я слежу, приближается к развязке, я хочу иметь реальную ставку на исходе, чтобы это было не просто новостью, а моим личным участием с настоящими последствиями.

**Персона:** Alex (News Junkie) — PRIMARY  
**Почему это MJ, а не функциональный job:**  
Это финальный прогресс, ради которого существует продукт. Все остальные jobs — либо шаги к нему, либо слои поверх него. Без MJ остальные jobs теряют смысл.

| Что подтверждает | Источник |
|---|---|
| JTBD J2: "follow events with real skin in the game" — primary JTBD, confirmed across all 3 research iterations | CLAUDE.md · master-research.md §1 Key Conclusions #1 |
| "Engaged spectator with skin in the game" — формулировка из strategy.md | master-research.md §3 How We're Solving It |
| News Junkie: "Prove they're right on current events" — сегмент подтверждён как primary | strategy.md · personas.md Persona 1 |

---

## FJ · Functional Jobs (путь к MJ)

Это шаги, без которых MJ невозможен. Каждый — точка возможного отвала по данным AARRR.

---

### FJ1 — Когда что-то важное происходит в мире и у меня есть мнение об исходе, я хочу быстро найти это событие среди активных ставок, чтобы не упустить момент, пока тема актуальна.

**Персона:** Alex (PRIMARY) · Dan (Crypto Native)  
**Отвал по AARRR:** Acquisition → Activation (первый шаг после прихода)

| Что подтверждает | Источник |
|---|---|
| "Event-triggered arrival — KEY pattern for all segments. Entry point." | ux-patterns.md — Audience Behavioral Patterns |
| "How we greet the user 'from the news' determines activation and the first bet" | master-research.md §6 |
| Path to AHA: Arrived → Registered → … → Found a market | aarrr.md — PATH TO AHA MOMENT |

---

### FJ2 — Когда я вижу событие и вероятностную оценку рядом с ним, я хочу понять, почему рынок считает именно так и что может изменить это число, чтобы принять осознанное решение, а не ставить вслепую.

**Персона:** Alex (PRIMARY)  
**Отвал по AARRR:** внутри Activation — между "Found a market" и "Understood the mechanics"

| Что подтверждает | Источник |
|---|---|
| ПОДТВЕРЖДЁН КАК ДИФФЕРЕНЦИАТОР: "No competitor explains 'why is the price this?'" | master-research.md §4 Gap table · §1 Key Conclusions #2 |
| "Markets are isolated questions without context. This is our differentiator." | ux-patterns.md — Story-driven Discovery Reason 2 |
| Benchmark: ни один из 5 продуктов не объясняет контекст цены внутри продукта | benchmark-trust.md C3 fee transparency + C8 resolution clarity |

---

### FJ3 — Когда я решил поставить, я хочу это сделать с обычными деньгами без изучения незнакомых технологий, чтобы барьер входа касался только события, а не инфраструктуры вокруг него.

**Персона:** Alex (PRIMARY)  
**Отвал по AARRR:** Activation — между "Registered" и "Fiat on-ramp" — главная точка дропаута

| Что подтверждает | Источник |
|---|---|
| RISKIEST ASSUMPTION PROXY: "The main barrier for News Junkie is needing MetaMask and USDC before the first bet" | master-research.md §7 H1 · strategy.md Riskiest Assumption |
| "8+ wallet icons = cognitive overload" на экране signup Polymarket | master-research.md §7 Gap #5 · screens/polymarket-signup-mobile.png |
| "No PM has solved onboarding without a Web3 wallet" | master-research.md §7 Gap #1 · competitive-analysis.md Q1 |
| "Onboarding assumes prior knowledge of the product type" | master-research.md §4 Competitor gaps |

---

### FJ4 — Когда я вижу незнакомую платформу и собираюсь положить туда реальные деньги, я хочу получить однозначный ответ на вопрос "что с ними случится", чтобы мой риск касался события, а не самой платформы.

**Персона:** Alex (PRIMARY) · Maria (Crossover Bettor)  
**Отвал по AARRR:** между "Fiat on-ramp" и "Placed bet" — страх перед депозитом

| Что подтверждает | Источник |
|---|---|
| "New fintech user's primary fear is 'what happens to my money'" | benchmark-trust.md Top 3 mechanisms #2 · hypothesis H4 |
| Futuur — ближайший аналог — C2 (Funds protection): 1/5. Polymarket: 1/5. Это открытый gap. | benchmark-trust.md scores |
| Revolut решает это одной фразой и получает C2: 5/5 — шаблон для нас | benchmark-trust.md Top 3 mechanisms #2 |
| 70–84% трейдеров теряют деньги — структурный факт рынка, усиливает этот страх | live-research F2 · Yahoo Finance / DeFi Oasis Dec 2025 |

---

### FJ5 — Когда событие разрешилось и я проиграл, я хочу понять, что именно произошло и увидеть следующий шаг, чтобы уйти с ощущением честной игры, а не импульсивно увеличить ставку.

**Персона:** Alex (PRIMARY) — особенно уязвим как новый пользователь  
**Отвал по AARRR:** Activation → Retention — потеря после первой ставки = главный риск оттока D7

| Что подтверждает | Источник |
|---|---|
| "Post-resolution experience is undesigned — especially for losses. No competitor has a 'here's what happened, here's next' loss screen." | master-research.md §4 Competitor gap table |
| Паттерн F3: после первой потери — не уход, а чейсинг и эскалация. Цитата: "then bam, everything's gone." | live-research F3 · AOL 2026 |
| "Losing first bet → doesn't return" — отмечен как ключевой риск в воронке | aarrr.md Funnel |
| "Post-resolution loss screen + prediction streak mechanic" — решение из v_refresh | master-research.md §3 AARRR Product Decisions |

---

## EJ · Emotional Jobs

Как человек хочет себя чувствовать в каждой точке пути. Работают параллельно FJ, не после.

---

### EJ1 — Когда моё предсказание оказалось верным, я хочу ощутить, что понимаю происходящее лучше большинства, чтобы это было подтверждением моего взгляда на мир, а не случайной удачей.

**Персона:** Alex (PRIMARY) — это его первичный мотив  

| Что подтверждает | Источник |
|---|---|
| "Prove they're right on current events" — формулировка мотивации сегмента | strategy.md · personas.md Persona 1 J1 |
| "Knowledge validation: user already has an opinion and comes to check whether the market agrees" | ux-patterns.md Audience Behavioral Patterns |
| JTBD J2: "skin in the game" — не про деньги, а про участие | CLAUDE.md · master-research.md §3 |

---

### EJ2 — Когда платформа впервые просит меня доверить ей деньги, я хочу чувствовать, что это серьёзная и прозрачная организация, чтобы моя тревога о безопасности средств ушла до того, как я нажму "подтвердить".

**Персона:** Alex (PRIMARY) · Maria (Crossover Bettor)  

| Что подтверждает | Источник |
|---|---|
| Trust — #1 value для аудитории 20–40 | CLAUDE.md Target Audience · benchmark-trust.md Why Trust |
| "Первый сбой доверия — когнитивная тревога ('что вообще это такое?')" | benchmark-trust.md Top 3 mechanisms #1 |
| Bet365 убирает тревогу мгновенно, C5: 5/5. Futuur — C5: 3/5. Polymarket — C5: 3/5. | benchmark-trust.md C5 Clarity of first impression |

---

### EJ3 — Когда я проиграл ставку, я хочу выйти из этого момента с ощущением, что понял что-то новое, а не с желанием отыграться, чтобы следующее решение было осознанным, а не эмоциональным.

**Персона:** Alex (PRIMARY) — особенно после первого проигрыша  

| Что подтверждает | Источник |
|---|---|
| F3: паттерн escalation — early wins → overconfidence → loss-chasing. Интервенция нужна именно здесь. | live-research F3 · AOL 2026 |
| "Post-resolution loss screen is the intervention point before chasing begins. No competitor designs this." | master-research.md §8 Key Implication |
| 19 федеральных исков против Kalshi к январю 2026 — контекст масштаба проблемы | live-research F3 |

---

## SJ · Social Jobs

Что человек хочет, чтобы увидели другие. Работает поверх всего пути.

---

### SJ1 — Когда я выиграл ставку на событие, о котором говорили все, я хочу легко показать это своему окружению, чтобы люди увидели: я понял исход раньше большинства.

**Персона:** Alex (PRIMARY) · в меньшей степени — все сегменты  

| Что подтверждает | Источник |
|---|---|
| "'I told you so' is a powerful social instinct. A win makes people want to show it off." | master-research.md §7 H5 |
| "Social sharing — wants to show prediction/win. Especially News Junkie." | ux-patterns.md Audience Behavioral Patterns |
| H5: Share card после каждой резолюции → >20% нового трафика через шэринг | aarrr.md Referral · hypothesis H5 |
| Robinhood и Spotify Wrapped подтвердили этот паттерн в других вертикалях | master-research.md §7 H5 |

---

### SJ2 — Когда я делаю прогнозы регулярно, я хочу, чтобы моя история была публично видна и проверяема, чтобы репутация человека "который понимает" строилась на фактах, а не на словах.

**Персона:** Alex (PRIMARY) · Dan (Crypto Native)  

| Что подтверждает | Источник |
|---|---|
| "Public prediction track record from day one (eToro CopyTrader model)" — добавлено в v_refresh | master-research.md §3 AARRR Product Decisions — Referral |
| "Profile: prediction track record as reputation" — в описании продукта | CLAUDE.md Product implications |
| Metaculus как референс — качество прогнозов как социальная валюта | master-research.md §4 Competitors — SOFT group |

---

## HJ · Гипотезы

Jobs без достаточной доказательной базы. Не включены в основной список. Требуют валидации.

---

### HJ1 (гипотеза) — Когда я понимаю ситуацию лучше рынка, я хочу конвертировать это в деньги максимально просто, чтобы знание давало материальный результат без сложности трейдинга.

**Персона:** (?) — предположительно Alex и Dan  
**Почему гипотеза:** CLAUDE.md называет это secondary JTBD. Исследование подтверждает J2 ("prove right") как первичный мотив. Деньги могут быть следствием, а не драйвером — но прямых данных нет.  
*Source: CLAUDE.md Secondary JTBD · personas.md Alex J4 (?)*

---

### HJ2 (гипотеза) — Когда я вижу, что рынок неправильно оценивает вероятность события, я хочу занять позицию до корректировки, чтобы зафиксировать преимущество от более точного анализа.

**Персона:** Dan (Crypto Native)  
**Почему гипотеза:** "Value hunting" подтверждён как паттерн для Crypto Native и Crossover, но нет прямых данных о том, что это первичный мотив именно для Dan в нашем продукте (vs. Polymarket).  
*Source: ux-patterns.md "Value hunting" · personas.md Dan J2 (?)*

---

### HJ3 (гипотеза) — Когда я хорошо разбираюсь в анализе спортивных событий, я хочу применить те же навыки к политике и новостям, чтобы мой аналитический подход работал за пределами спорта.

**Персона:** Maria (Crossover Bettor) — post-MVP сегмент  
**Почему гипотеза:** сегмент помечен "Later". Мотив логически вытекает из описания, но прямых данных — интервью, форумов, отзывов — нет.  
*Source: personas.md Persona 3 J1 (?) · strategy.md Crossover Bettor description*

---

### HJ4 (гипотеза) — Когда я хочу попробовать платформу без риска, я хочу сначала поиграть с виртуальными деньгами, чтобы понять механику до реальной ставки.

**Персона:** (?) — предположительно Alex при первом контакте  
**Почему гипотеза:** интуитивно выглядит как барьер — но live-research F1 прямо опровергает эффективность play-money как пути к реальным деньгам. Manifold протестировал и закрыл. Job может существовать у пользователя, но его выполнение не конвертирует в MJ.  
*Source: live-research F1 · Manifold blog Feb 2025 — прямое опровержение*

---

## Чего не знаем об этих jobs

| Вопрос | Влияние |
|---|---|
| Действительно ли Alex хочет ставить деньги — или просто наблюдать? (Riskiest Assumption) | Подтверждает или опровергает весь MJ для Primary персоны |
| Какой минимальный размер ставки делает FJ3 "настоящим"? | FJ3 — порог входа |
| Какое конкретное событие первым приводит Alex на платформу? | FJ1 — точка входа в воронку |
| Что именно говорят пользователи о моменте после потери — в их словах? | FJ5 + EJ3 — нет верифицированных цитат |

*Source: master-research.md §8 Open questions Q1, Q3, Q5 · live-research Q1, Q3, Q5, Q7*

---

*Compiled from: CLAUDE.md · personas.md · master-research.md · strategy.md · ux-patterns.md · aarrr.md · benchmark-trust.md · live-research F1–F3 (June 2026)*

---

## JTBD Matrix

> Важливість: **3** = критична (job = причина прийти/залишитися) · **2** = релевантна · **1** = незначна · **[?]** = даних немає, не середнє
> ФУНКЦІЯ = що в нашому продукті закриває цей job
> КОНКУРЕНТИ = чи закривають гравці з research.md (Polymarket · Kalshi · Futuur · Bet365 · Revolut)

---

| Job | Alex ⭐ Primary | Dan 🥈 Secondary | Maria 🥉 Secondary | ФУНКЦІЯ | КОНКУРЕНТИ |
|---|---|---|---|---|---|
| **MJ** Реальна ставка на подію | **3** — JTBD J2 primary, підтверджено в усіх 3 ітераціях ресёрчу | **2** — той самий job, вже на Polymarket, менша гострота | **2** — новий домен для досвідченого бетора | Флоу події → YES/NO → підтвердження | Polymarket ✓ Kalshi ✓ (US only) Futuur ✓ — всі закривають, але не для аудиторії Алекса |
| **FJ1** Знайти подію поки актуальна | **3** — "Event-triggered arrival = KEY for all segments" · ux-patterns.md | **2** — орієнтується самостійно | **2** — звик до фідів Bet365 | Фід подій зі стислим контекстом (не просто заголовки) | Polymarket ✓ Kalshi ✓ Futuur ✓ — всі мають фіди, але без наративу навколо події |
| **FJ2** Чому саме ця ймовірність | **3** — ПІДТВЕРДЖЕНИЙ ДИФЕРЕНЦІАТОР · "no competitor explains 'why this price?'" · master-research.md §4 | **1** — розуміє ринки, пояснення не потрібне | **2** — грамотний з odds, але новачок у PM | Story-driven блок контексту на сторінці події | **НІХТО** · Підтверджений gap у всіх 5 бенчмаркованих продуктах · master-research.md §4 gap table |
| **FJ3** Поповнити рахунок без крипто | **3** — RISKIEST ASSUMPTION PROXY · головна точка дропауту · master-research.md §7 H1 | **1** — немає бар'єру, є MetaMask | **2** — немає крипто, потрібен картковий шлях | Fiat on-ramp (картка → USDC) з першого екрану після реєстрації | Kalshi ✓ але US only · Futuur [?] частково · Polymarket через MoonPay але не UX-пріоритет (C6: 2/5) · Інші: ні |
| **FJ4** Впевнитися що гроші в безпеці | **3** — головний страх перед депозитом · benchmark-trust.md C2 · hypothesis H4 | **2** — on-chain верифікація важлива | **3** — референс Bet365 (C2: 4/5), дуже чутлива до ліцензій | Один рядок захисту коштів на екрані депозиту + on-chain підтвердження | Bet365 ✓ C2: 4/5 · Revolut ✓ C2: 5/5 · **Polymarket ✗ C2: 1/5 · Futuur ✗ C2: 1/5** · Gap 14–19 pts нижче референсу |
| **FJ5** Пережити першу поразку без чейсингу | **3** — F3: паттерн ескалації підтверджено · головний ризик D7 retention | **2** — актуально, менш гостро (досвід) | **2** — досвід ставок допомагає, але ризик є | Екран після резолюції для програшу ("що сталося + наступний крок") | **НІХТО** · "no competitor has a 'here's what happened, here's next' loss screen" · master-research.md §4 |
| **EJ1** Відчути що я розумію краще за більшість | **3** — "I told you so" — первинний драйв Алекса · personas.md J1 · ux-patterns.md Knowledge validation | **2** — другорядне відносно грошей | **[?]** — немає даних: для неї важливіше виграти чи довести правоту? | [?] не визначено — кандидати: win-screen, "you were right" copy, prediction history | Metaculus ✓ частково (прогнози як репутація, але play-money) · Polymarket/Kalshi: частково (share) |
| **EJ2** Відчути безпеку коштів | **3** — той самий страх що FJ4, але емоційний шар на кожному екрані | **2** — on-chain докази важливі | **3** — критично, Bet365 = референсна планка (33/40) | Довірчий текст на екрані депозиту · "Your USDC is held 1:1" | Bet365 ✓ C2: 4/5 · Revolut ✓ C2: 5/5 · **Polymarket ✗ 1/5 · Futuur ✗ 1/5** |
| **EJ3** Вийти з поразки усвідомлено | **3** — F3: потрібна інтервенція до початку чейсинг-петлі · live-research F3 | **1** — керує собою самостійно | **2** — досвід бетора є, але ризик залишається | Той самий екран що FJ5 (одна функція закриває два jobs) | **НІХТО** · жоден конкурент не проектує цей момент |
| **SJ1** Показати що був правий | **3** — "I told you so" — найсильніший соціальний мотив · ux-patterns.md Social sharing · H5 | **2** — другорядне | **[?]** — немає даних для бетора зі спорту | Автоматична share-картка після резолюції (модель Robinhood) | Polymarket ✓ частково (shareable links) · Kalshi ✓ частково · **Автоматичних карток немає ні в кого** |
| **SJ2** Накопичити публічний трек-рекорд | **2** — релевантно, але вторинне відносно SJ1 | **3** — репутація "розумного трейдера" — первинна | **[?]** — немає даних | Публічний профіль прогнозів (модель eToro CopyTrader) · aarrr.md v_refresh | Metaculus ✓ (play-money) · eToro ✓ (інший продукт) · Polymarket: частково · **Прямі PM конкуренти: не закривають** |

---

## Висновок: 3 jobs в ядро MVP

Критерії відбору: **Alex = 3** + **не закриті ринком** (або закриті тільки поза нашим гео/аудиторією).

---

### MVP Job 1 — FJ2: Чому саме ця ймовірність

**Alex: 3 · НІХТО не закриває**

Єдиний підтверджений диференціатор у всьому ресёрчі. Жоден із 5 бенчмаркованих продуктів не пояснює контекст ціни всередині продукту. Це одночасно наш головний gap і наш головний аргумент для News Junkie.

→ **Функція-кандидат:** story-driven блок контексту на сторінці кожної події (наратив + чому ціна = X + умови резолюції)

*master-research.md §4 gap table · benchmark-trust.md усі 5 продуктів · ux-patterns.md Story-driven Reason 2*

---

### MVP Job 2 — FJ3: Поповнити рахунок без крипто

**Alex: 3 · Закриває тільки Kalshi (US only, не наша аудиторія)**

Головна точка дропауту на шляху до AHA-моменту. Якщо Riskiest Assumption вірна (бар'єр = тертя, не мотивація) — це єдине що стоїть між Alex і першою ставкою. Без цього MVP не тестує гіпотезу.

→ **Функція-кандидат:** fiat on-ramp (картка → USDC) з першого екрану після реєстрації, без редиректу на сторонній сервіс

*master-research.md §7 H1 · aarrr.md PATH TO AHA · competitive-analysis.md Q1*

---

### MVP Job 3 — FJ5 + EJ3: Пережити першу поразку без чейсингу

**Alex: 3 · НІХТО не проектує цей момент**

70–84% користувачів PM програють гроші (F2). Паттерн після поразки — не вихід, а ескалація (F3). Жоден конкурент не має екрану між "програв" і "наступна ставка". Це найбільший ризик D7 retention і єдина точка, де ми можемо розірвати чейсинг-петлю.

→ **Функція-кандидат:** post-resolution loss screen: пояснення результату + один чіткий наступний крок (не промо нової ставки)

*live-research F2 + F3 · master-research.md §4 gap "post-resolution undesigned" · aarrr.md Retention "first-bet loss"*

---

## Функції-кандидати на виліт

Функції, які не закривають жодного job з Alex-рядка зі значенням 3, або закривають тільки гіпотетичні jobs.

| Функція | Який job закриває | Чому на виліт |
|---|---|---|
| **Demo bet / play-money режим** | HJ4 (гіпотеза) | F1: Manifold протестував і закрив. Play-money не конвертує в реальні гроші. Закриває job якого у Alex немає. |
| **Market Board / Trading view** | HJ2 (Dan, гіпотеза) | Прямо відхилений для primary аудиторії в ux-patterns.md. "Мова трейдера, не глядача." Для Alex — дропаут. |
| **Спортивні ринки на MVP** | HJ3 (Maria, post-MVP) | Рішення прийнято: post-MVP з 3-місячним чекпоінтом. Не закриває жодного job Alex. Додає складність без перевірки ядра. |

*master-research.md §1 Key Conclusions #6 · live-research F1 · ux-patterns.md "❌ Not a Fit: Market Board"*
