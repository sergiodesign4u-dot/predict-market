# Competitive Analysis

## Screens Index

| Файл | Платформа | Екран | Доступ |
|---|---|---|---|
| `polymarket-home-mobile.png` | Polymarket | Головна — фід ринків, категорії, YES/NO картки | Public |
| `polymarket-home-scroll-mobile.png` | Polymarket | Головна — скрол, live спорт-ринки | Public |
| `polymarket-event-detail-mobile.png` | Polymarket | Деталь події — мультиаутком, графік, обсяг | Public |
| `polymarket-event-bet-mobile.png` | Polymarket | Інтерфейс ставки — Buy Yes/No в центах | Public |
| `polymarket-signup-mobile.png` | Polymarket | Sign Up — Google + Email + 8 wallet-іконок | Public |
| `kalshi-home-mobile.png` | Kalshi | Головна + авто-модал реєстрації | Public |
| `kalshi-home-browse-mobile.png` | Kalshi | Головна після закриття — LIVE hero-картка | Public |
| `kalshi-market-detail-mobile.png` | Kalshi | Деталь ринку — свічковий графік, price brackets | Public |
| `manifold-home-mobile.png` | Manifold | Головна — список питань, play money | Public |
| `manifold-market-detail-mobile.png` | Manifold | Деталь ринку — % chance, Bet YES/NO, коменти | Public |
| `futuur-home-mobile.png` | Futuur | Головна — мультиаутком з probability bars | Public |
| `futuur-market-detail-mobile.png` | Futuur | Деталь ринку — графік, outcomes | Public |
| `futuur-market-bet-mobile.png` | Futuur | Bet interface — Yes/No per outcome | Public |
| `metaculus-home-mobile.png` | Metaculus | Головна — question feed, gauge charts | Public |
| `metaculus-question-detail-mobile.png` | Metaculus | Деталь питання — 65% gauge, Predict, коменти | Public |
| Portfolio / My Bets | Polymarket | Відкриті позиції, P&L | **[? за логіном]** |
| Portfolio / My Bets | Kalshi | Портфель, history | **[? за логіном]** |
| Deposit flow | Polymarket | Крипто-депозит, on-ramp | **[? за логіном]** |
| Deposit flow | Kalshi | Фіат-депозит, ACH/card | **[? за логіном]** |
| Deposit flow | Futuur | Crypto + fiat вибір | **[? за логіном]** |
| Leaderboard | Futuur | Ranking юзерів | **[? за логіном]** |

---

## Порівняльна таблиця

| Вісь | Polymarket | Kalshi | Manifold | Futuur | Metaculus |
|---|---|---|---|---|---|
| **Аудиторія** | Крипто-нейтіви, DeFi-юзери, глобально (не США) | США, TradFi-аудиторія, mainstream | Глобально, всі — без бар'єру реальних грошей | Глобально, крипто + fiat hybrid | Аналітики, дослідники, policy-спільнота |
| **Основа продукту** | CLOB на Polygon, pUSD (USDC) | CFTC-регульована біржа, USD фіат | Play money (Mana Ṁ), user-created markets | Крипто + fiat hybrid, мульти-валюта | Без грошей — чисте forecasting + репутація |
| **Ключові механізми** | Conditional Token Framework, YES/NO бінарні токени, order book matching | Order book, ціна в центах (82¢/19¢), regulated settlement | AMM для маркет-мейкінгу, AI-generated context, community resolution | Probability bars per outcome, Yes/No на кожен варіант | Aggregated community forecast, calibration scoring |
| **Довіра** | On-chain прозорість, UMA decentralized resolution, $7.5B+ обсяг | CFTC-регуляція — найвища інституційна довіра | Немає ризику реальних грошей — довіра через відкритість | Менш відомий, невеликий трек-рекорд | Академічна точність (~4% відхилення), партнерства |
| **Монетизація** | ~2% fee з виграшів + maker/taker rebates | Exchange fees (maker/taker), як класична біржа | Prize pool drawings в USDC, без fees на Mana-торги | Комісія з ставок (% не публічний) | Гранти, інституційні партнерства, premium |

---

## 3 Спільні патерни

**1. Горизонтальна категорійна навігація вгорі + bottom tab bar**
Всі без винятку використовують один і той самий паттерн: горизонтальний скрол категорій (Trending, Politics, Crypto…) і нижня навігація з 3–5 табів. Це де-факто стандарт жанру.

**2. Відсоток ймовірності як головне число**
На кожній картці і на кожному детальному екрані — % probability є центральним елементом. Він стоїть більше за назву події, більше за обсяг. Це "ціна" ринку і одночасно "стан гри".

**3. Графік зміни ймовірності в часі**
Усі платформи (крім Metaculus частково) показують як рухалась ціна — від простої лінії (Manifold) до свічкового графіка (Kalshi). Динаміка = залученість. Люди повертаються дивитись чи їхня позиція "в плюсі".

---

## 3 Ключові відмінності

**1. Механіка ціноутворення: CLOB vs AMM vs Community**
- Polymarket і Kalshi: order book — ціна формується зустрічними ордерами
- Manifold: AMM — ліквідність автоматична, ринок завжди є
- Metaculus: агрегат прогнозів спільноти, без торгівлі
→ **Наслідок:** CLOB дає "чесніші" ціни але вимагає ліквідності. AMM завжди працює але може дати гірший курс.

**2. Реальні гроші vs Play money vs Crypto**
- Kalshi: фіат USD, CFTC-регуляція — найбільша довіра, але географічно обмежений
- Polymarket: крипто (USDC на Polygon) — глобальний, але Web3-бар'єр
- Manifold: play money — нульовий бар'єр, але й нульова ставка
→ **Наслідок:** кожен підхід бере різну аудиторію. Hybrid (Futuur) теоретично найширший.

**3. Хто створює ринки**
- Polymarket, Kalshi: команда платформи — контроль якості, менше ринків
- Manifold: будь-який юзер — тисячі ринків, але якість різна
- Metaculus: mix — модеровані питання + community
→ **Наслідок:** Platform-created = curated і trustworthy. User-created = scale але і сміття.

---

## 3 Відкритих питання

**1. Як вирішити проблему першої ставки без Web3-гаманця?**
Polymarket технічно вимагає USDC на Polygon. Kalshi вимагає US-банк. Futuur — найбільш hybrid, але незрозуміло як точно. Жоден не вирішив онбординг для "звичайного юзера" бездоганно. Чи fiat card → stablecoin on-ramp може бути нашою перевагою?

**2. CLOB чи AMM для MVP?**
CLOB дає кращу ціну але вимагає ліквідності з першого дня (курка і яйце). AMM завжди працює але складніше пояснити юзеру. Що реалістичніше для запуску з нуля?

**3. Як побудувати довіру до resolution без регуляції і без великого track record?**
Kalshi вирішує через CFTC. Polymarket через UMA (децентралізований арбітраж). Обидва рішення складні для MVP. Чи достатньо прозорих правил + мультисиг команди на старті — чи це одразу відштовхне юзерів?
