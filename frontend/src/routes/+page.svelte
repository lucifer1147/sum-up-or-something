<script>
	import src from '$lib/assets/Designer.jpeg';

</script>

<div class="flex justify-center items-center h-[100vh] overflow-hidden relative">
	<img {src} alt="computers" class="w-full absolute z-[-10]" />
	<div
		class="bg-slate-900 h-full w-full bg-opacity-80 backdrop-blur-sm flex justify-center items-center p-40"
	>
		<div class="w-2/3">
			<h1 class="text-white text-6xl font-mono font-extrabold text-center mb-10">SumUp</h1>
			<p class="text-white text-lg font-mono font-semibold mb-10">
				Lorem ipsum dolor sit, amet consectetur adipisicing elit. Provident similique ipsa inventore
				fugiat excepturi autem dolores, adipisci eius doloribus quasi facere earum eum in nulla a
				deserunt quia voluptas consequuntur temporibus modi aliquid consectetur libero soluta.
				Facilis repellendus dolor sit!
			</p>

			<div class="flex justify-evenly">
				<div
					class="bg-gray-800 h-12 w-1/2 mr-5 font-mono font-semibold text-xl text-white rounded-xl"
					>
					<a href="/login" class="w-full h-full flex justify-center items-center">Login</a>
				</div>
				<div
					class="bg-gray-800 h-12 w-1/2 font-mono font-semibold text-xl text-white rounded-xl"
					>
					<a href="/signup" class="w-full h-full flex justify-center items-center">SignUp</a>
				</div>
			</div>
		</div>
	</div>
</div>
