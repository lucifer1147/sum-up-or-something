<script>
	import Singupdiv from './singupdiv.svelte';
	import { signupdone } from './store.js';
</script>

<div
	class="bg-gradient-to-l from-slate-900 to-slate-800 h-[100vh] flex justify-center items-center backdrop-blur-lg"
>
	<div
		class="bg-white backdrop-opacity-45 w-2/3 h-[100vh] rounded-2xl flex justify-center items-center flex-wrap overflow-auto"
	>
		{#if !$signupdone}
			<Singupdiv />
		{:else}
			<p class="text-4xl font-black w-full text-center opacity-100">
				Check your email to activate your account!
			</p>
		{/if}
	</div>
</div>
