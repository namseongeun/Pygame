#-*-coding:utf-8-*-
import sys
from fpdf import FPDF

sys.stdout.reconfigure(encoding='utf-8')

# Create a PDF class
class PDF(FPDF):
    def header(self):
        self.set_font("Arial", "B", 14)
        self.cell(0, 10, "CRA 1차 시험 요약 정리 (기초통계 / 기업신용분석 / 여신심사 및 관리)", ln=True, align="C")
        self.ln(5)

    def chapter_title(self, title):
        self.set_font("Arial", "B", 12)
        self.set_text_color(0)
        self.cell(0, 10, title, ln=True)
        self.ln(3)

    def chapter_body(self, body):
        self.set_font("Arial", "", 10)
        self.multi_cell(0, 8, body)
        self.ln()

# Initialize PDF
pdf = PDF()
pdf.add_page()

# Content for each subject
stat_text = """
[1. 기초통계 요약]

- 기술통계: 평균, 분산, 표준편차, 공분산, 상관계수
- 확률분포: 이산분포(베르누이, 이항 등), 연속분포(정규, t, F 분포 등)
- 추정과 가설검정:
  * 중심극한정리, 신뢰구간
  * 가설검정의 절차: 영가설/대립가설 → 검정통계량 → p값 → 결론
- 회귀분석:
  * 단순회귀: Y = β₀ + β₁X + ε
  * 잔차분석, 결정계수(R²)
- 시계열 분석 기초:
  * 이동평균(MA), 지수가중이동평균(EWMA)
  * 추세, 계절성, 자기상관계수 등
"""

credit_text = """
[2. 기업신용분석 요약]

- 신용분석 목적: 채무불이행 가능성 사전 분석
- 정량적 분석: 재무비율 (유동비율, 부채비율, 이자보상비율 등)
- 정성적 분석: 경영역량, 시장지위, 산업위험 등
- 신용등급 결정:
  * 재무정보 + 산업동향 + 기업운영 종합평가
- 신용등급 변동요인:
  * 외부환경, 재무악화, 투자확대, 구조조정 등
- 스코어링 모형 및 Z-score:
  * 파산 예측 모델로 객관적 수치화
- 사례 분석: 업종별 위험요인, 부실 징후, 대응 전략
"""

loan_text = """
[3. 여신심사 및 관리 요약]

- 여신심사 절차:
  * 신청 → 분석 → 심사 → 승인
- 론 리뷰(LRR): 기존 대출의 정기적 사후 평가
- 사후관리:
  * 재무변화 감시, 조건 준수 여부, 등급 재조정
- 기업가치 평가:
  * DCF법, PER, EVA 등 활용
- 담보 및 보증 분석:
  * 담보가치 평가, 회수 가능성
- 워크아웃 4원칙:
  * 자구노력, 공동협의, 채무조정, 신규자금 지원
- 부실징후: 매출급감, 이자미납, 자본잠식 등
"""

# Add chapters to PDF
pdf.chapter_title("1. 기초통계")
pdf.chapter_body(stat_text)

pdf.chapter_title("2. 기업신용분석")
pdf.chapter_body(credit_text)

pdf.chapter_title("3. 여신심사 및 관리")
pdf.chapter_body(loan_text)

# Output the PDF
pdf.output("CRA_1차_요약정리.pdf")