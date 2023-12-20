# [Diamond III] Qanat - 10791 

[문제 링크](https://www.acmicpc.net/problem/10791) 

### 성능 요약

메모리: 31120 KB, 시간: 40 ms

### 분류

미적분학, 수학

### 제출 일자

2023년 12월 11일 17:13:25

### 문제 설명

<p>A qanat is an irrigation system widely used to deliver water in hot, arid climates. The technology was originally developed by Persians over 2000 years ago. In Morocco, qanats are known as khettara and are still used today in the southern part of the country.</p>

<p>The basic feature of a qanat is an essentially horizontal channel that brings water from an underground water source to an outlet near a civilization. There is also a shaft known as a mother well that rises vertically from the underground water source to the surface of a mountain or hill. Creating such a system is extremely expensive, and was especially so in ancient times, since all of the materials excavated from the channel and mother well must be carried above ground, either through the channel outlet or the top of the mother well. To aid in the construction, there are often one or more additional vertical shafts placed at strategic locations above the underground channel. Although these shafts must also be excavated, they provide a means for lifting additional dirt from the horizontal channel as illustrated in Figure H.1.</p>

<p style="text-align:center"><img alt="" src="https://onlinejudgeimages.s3-ap-northeast-1.amazonaws.com/problem/10791/1.png" style="height:183px; width:347px"></p>

<p style="text-align:center">Figure H.1: An illustration of a qanat.</p>

<p>For this problem, model the cross-section of a qanat as shown in Figure H.2, with the channel outlet at (0, 0), the water source at (w, 0), and the top of the mother well at (w, h) with w > h. The surface of the mountain extends along a straight line from (w, h) to (0, 0).</p>

<p style="text-align:center"><img alt="" src="https://onlinejudgeimages.s3-ap-northeast-1.amazonaws.com/problem/10791/2.png" style="height:128px; width:316px"></p>

<p style="text-align:center">Figure H.2: A simplified model of a qanat cross-section.</p>

<p>Every qanat must have a vertical mother well from the water source to the mountain surface above, along with n additional vertical shafts. The channel and all shafts are modeled as line segments. Your goal is to determine the placement for those additional shafts so as to minimize the overall excavation cost. This cost is equal to the sum of the distances that each piece of excavated dirt must be transported to reach the surface (using any combination of horizontal and vertical movement). For example, the cost of excavating a continuous section of dirt starting from the surface and going along a path of length <mjx-container class="MathJax" jax="CHTML" style="font-size: 109%; position: relative;"><mjx-math class="MJX-TEX" aria-hidden="true"><mjx-mi class="mjx-i"><mjx-c class="mjx-c2113"></mjx-c></mjx-mi></mjx-math><mjx-assistive-mml unselectable="on" display="inline"><math xmlns="http://www.w3.org/1998/Math/MathML"><mi>ℓ</mi></math></mjx-assistive-mml><span aria-hidden="true" class="no-mathjax mjx-copytext">\(ℓ\)</span></mjx-container> (possibly including turns) is <mjx-container class="MathJax" jax="CHTML" style="font-size: 109%; position: relative;"><mjx-math class="MJX-TEX" aria-hidden="true"><mjx-msubsup><mjx-mo class="mjx-sop"><mjx-c class="mjx-c222B TEX-S1"></mjx-c></mjx-mo><mjx-script style="vertical-align: -0.341em; margin-left: -0.138em;"><mjx-texatom size="s" texclass="ORD" style="margin-left: 0.276em;"><mjx-mi class="mjx-i"><mjx-c class="mjx-c2113"></mjx-c></mjx-mi></mjx-texatom><mjx-spacer style="margin-top: 0.388em;"></mjx-spacer><mjx-texatom size="s" texclass="ORD"><mjx-mn class="mjx-n"><mjx-c class="mjx-c30"></mjx-c></mjx-mn></mjx-texatom></mjx-script></mjx-msubsup><mjx-texatom space="2" texclass="ORD"><mjx-mi class="mjx-i"><mjx-c class="mjx-c1D465 TEX-I"></mjx-c></mjx-mi><mjx-mi class="mjx-i"><mjx-c class="mjx-c1D451 TEX-I"></mjx-c></mjx-mi><mjx-mi class="mjx-i"><mjx-c class="mjx-c1D465 TEX-I"></mjx-c></mjx-mi></mjx-texatom><mjx-mo class="mjx-n" space="4"><mjx-c class="mjx-c3D"></mjx-c></mjx-mo><mjx-mfrac space="4"><mjx-frac><mjx-num><mjx-nstrut></mjx-nstrut><mjx-mn class="mjx-n" size="s"><mjx-c class="mjx-c31"></mjx-c></mjx-mn></mjx-num><mjx-dbox><mjx-dtable><mjx-line></mjx-line><mjx-row><mjx-den><mjx-dstrut></mjx-dstrut><mjx-mn class="mjx-n" size="s"><mjx-c class="mjx-c32"></mjx-c></mjx-mn></mjx-den></mjx-row></mjx-dtable></mjx-dbox></mjx-frac></mjx-mfrac><mjx-msup><mjx-mi class="mjx-i"><mjx-c class="mjx-c2113"></mjx-c></mjx-mi><mjx-script style="vertical-align: 0.363em;"><mjx-mn class="mjx-n" size="s"><mjx-c class="mjx-c32"></mjx-c></mjx-mn></mjx-script></mjx-msup></mjx-math><mjx-assistive-mml unselectable="on" display="inline"><math xmlns="http://www.w3.org/1998/Math/MathML"><msubsup><mo data-mjx-texclass="OP">∫</mo><mrow data-mjx-texclass="ORD"><mn>0</mn></mrow><mrow data-mjx-texclass="ORD"><mi>ℓ</mi></mrow></msubsup><mrow data-mjx-texclass="ORD"><mi>x</mi><mi>d</mi><mi>x</mi></mrow><mo>=</mo><mfrac><mn>1</mn><mn>2</mn></mfrac><msup><mi>ℓ</mi><mn>2</mn></msup></math></mjx-assistive-mml><span aria-hidden="true" class="no-mathjax mjx-copytext">\(\int _{ 0 }^{ ℓ }{ x dx }  = \frac{1}{2}ℓ^2\)</span></mjx-container>.</p>

### 입력 

 <p>The input consists of a single line containing three integers w (1 ≤ w ≤ 10 000), h (1 ≤ h < w), and n (1 ≤ n ≤ 1 000). The value w is the horizontal distance from the water source to the qanat outlet. The value h is the vertical distance from the water source to the mountain surface. The value n is the number of vertical shafts that must be used in addition to the mother well.</p>

### 출력 

 <p>First, display the minimum overall excavation cost. Next, display the x-coordinates, in increasing order, for n optimally placed vertical shafts. If n > 10, display only the first 10 x-coordinates. Answers within an absolute or relative error of 10<sup>−4</sup> will be accepted. You may assume that there is a unique solution. No test case will result in a shaft within 0.001 units from the outlet of the qanat channel or from another shaft.</p>

